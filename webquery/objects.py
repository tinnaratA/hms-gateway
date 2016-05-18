class Employee:

    empCount = 0

    def __init__(self, row_id, hn, title, first_name, last_name):

        self.row_id = row_id
        self.hn = hn
        self.title = title
        self.first_name = first_name
        self.last_name = last_name
        Employee.empCount += 1

    def displayCount(self):
        print ("Total Employee %d") % Employee.empCount

    def displayEmployee(self):
        print ("First Name: ", self.first_name , "Last Name: ", self.last_name)

    def __str__(self):
        sb = []
        for key in self.__dict__:
            sb.append("{key}='{value}'".format(key=key, value=self.__dict__[key]))
        return ', '.join(sb)

    def __repr__(self):
        return self.__str__()
