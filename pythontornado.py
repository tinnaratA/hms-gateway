import sys
import os

import tornado.httpserver
import tornado.ioloop
import tornado.web

# django settings must be called before importing models
from django.conf import settings
settings.configure(DATABASE_ENGINE='sqlite3', DATABASE_NAME='db')

from django import forms
from django.db import models

# Define your Model
class Message(models.Model):
    """
    A Django model class.
    In order to use it you will need to create the database manually.

    sqlite> CREATE TABLE message (id integer primary key, subject varchar(30), content varchar(250));
    sqlite> insert into message values(1, 'subject', 'cool stuff');
    sqlite> SELECT * from message;
    """

    subject = models.CharField(max_length=30)
    content = models.TextField(max_length=250)
    class Meta:
        app_label = 'dj'
        db_table = 'message'
    def __unicode__(self):
        return self.subject + "--" + self.content

# Define your Form
class DjForm(forms.Form):
    subject = forms.CharField(max_length=100, required=True)
    content = forms.CharField()

# Define the class that will respond to the URL
class ListMessagesHandler(tornado.web.RequestHandler):
    def get(self):
        messages = Message.objects.all()
        self.render("templates/index.html", title="My title",
                    messages=messages)

class FormHandler(tornado.web.RequestHandler):
    def get(self):
        form = DjForm()
        self.render("templates/form.html", title="My title", form=form)

    def post(self):
        data = {
            'subject':self.request.arguments['subject'][0],
            'content':self.request.arguments['content'][0],
        }
        form = DjForm(data=data)
        if form.is_valid():
            message = Message(**form.cleaned_data)
            message.save()
            self.redirect('/')
        else:
            self.render("templates/form.html", title="My title", form=form)

# map the Urls to the class
application = tornado.web.Application([
    (r"/", ListMessagesHandler),
    (r"/form/", FormHandler),
])

# Start the server
if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8889)
    tornado.ioloop.IOLoop.instance().start()
