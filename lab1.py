import requests

url = input('Write here a URL: ')

with requests.get(url) as response:
    for header in response.headers:
        print(header + " : " + response.headers[header])

