#uses the requests library 
import requests

payload = {'token': 'cac21dc164e91217722bb4a3da2320f4', 'github': 'https://www.github.com/mitchellmendoza/repo2endallrepos'}

#register by POSTing to endpoint
r1 = requests.post("http://challenge.code2040.org/api/register", data=payload)
