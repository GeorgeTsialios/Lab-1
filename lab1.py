import requests

url = input('Write here a URL: ')

with requests.get(url) as response:
    print(response.headers)

