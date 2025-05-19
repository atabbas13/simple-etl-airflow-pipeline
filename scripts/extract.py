# Extract script
import requests
import json

def extract():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    data = response.json()
    return data
