#uses the requests library 
import requests

payload = {'token': 'cac21dc164e91217722bb4a3da2320f4'}

#run a simple http post requests to the first endpoint to receive our string to reverse
r1 = requests.post("http://challenge.code2040.org/api/reverse", data=payload)

#reverse the string using extended slice syntax, and using a reverse slice. 
reversedStr = r1.text[::-1]

#add the new key value pair to our dictionary for the validation request
payload['string'] = reversedStr

#execute the validation request
r2 = requests.post("http://challenge.code2040.org/api/reverse/validate", data=payload)
