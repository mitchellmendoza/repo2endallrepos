import requests

payload = {'token': 'cac21dc164e91217722bb4a3da2320f4'}

#run a simple http post requests to the first endpoint to receive our string to reverse
r1 = requests.post("http://challenge.code2040.org/api/reverse", data=payload)

#sanity check
print(r1.text);

#reverse the string using python magic
reversedStr = r1.text[::-1];

#add the new key value pair to our dictionary for the validation request
payload['string'] = reversedStr;

#execute the validation request
r = requests.post("http://challenge.code2040.org/api/reverse/validate", data=payload)