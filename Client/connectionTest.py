import requests

response = requests.post(
	'http://10.105.107.92:8000/o/token/',
        data={
        	'grant_type': 'password',
        	'username': 'admin',
        	'password': 'admin@1234',
                'client_id': 'YBwnuoa49VQcbxfQypXOe3QScJgOUiBf5yblTUpP',
                'client_secret': '1i3uUxoxNmRYTQKCmlFFeh0pFhcxUglzFZ0qBFTVlEnXyQIOl47RIJG4nPFu53Z5OKnFhnzVXmrJbbmnw5JEGulBOpRiN45UiLscxznsRNbv85Qife19rKhXovPJJ8bE'
        }
)

print(response)
