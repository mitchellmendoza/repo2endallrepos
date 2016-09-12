#uses the requests library 
import requests

payload = {'token': 'cac21dc164e91217722bb4a3da2320f4'}

#acquire dictionary
r1 = requests.post("http://challenge.code2040.org/api/haystack", data=payload)
#requests library includes a json decoder, which will let me access the response as a JSON dictionary
dictionary = r1.json();
needle = dictionary['needle']
haystack = dictionary['haystack']
#loop through until we find the needle string, keep track of our index using a var
index = 0;
for string in haystack:
	if string == needle:
		break
	else: 
		index += 1
payload['needle'] = index
r2 = requests.post("http://challenge.code2040.org/api/haystack/validate", data=payload)
