#uses the requests library 
import requests

payload = {'token': 'cac21dc164e91217722bb4a3da2320f4'}
#acquire dictionary
r1 = requests.post("http://challenge.code2040.org/api/prefix", data = payload)
#requests library includes a json decoder, which will let me access the response as a JSON dictionary
dictionary = r1.json()
prefix = dictionary['prefix']
arr = dictionary['array']
new_arr = []
for string in arr:
	if string.startswith(prefix) == False:
		#add this string to a new array
		new_arr.append(str(string))

payload['array'] = new_arr
r2 = requests.post("http://challenge.code2040.org/api/prefix/validate", json = payload )

