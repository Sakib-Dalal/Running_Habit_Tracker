import requests
from datetime import datetime

# refer to the document: https://docs.pixe.la/
# https://pixe.la/

# Create user, token and graph before using code
USER_NAME = '<user_name>'
TOKEN = '<token>'

pixela_endpoint = 'https://pixe.la/v1/users'

graph_endpoint = f'{pixela_endpoint}/{USER_NAME}/graphs/<graphID>'

headers = {
    'X-USER-TOKEN': TOKEN
}

today = datetime.now().date().strftime(format='%Y%m%d')
running = input("Enter how many Km you run 🏃today: ")

graph_data = {
    'date': today,
    'quantity': running
}

response = requests.post(url=graph_endpoint, json=graph_data, headers=headers)

print(response.text)
