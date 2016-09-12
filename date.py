
#uses the requests library 
import requests
#uses arrow library
import arrow

payload = {'token': 'cac21dc164e91217722bb4a3da2320f4'}

#acquire dictionary
r1 = requests.post("http://challenge.code2040.org/api/dating", data=payload)
dictionary = r1.json()
timestamp = dictionary ['datestamp']
date = arrow.get(timestamp)
num_seconds = dictionary['interval']
converted_date = date.replace(seconds=+num_seconds)
#replace the daylight savings addition with a zulu to get back to original datestamp
date_str = str(converted_date).replace('+00:00', 'Z')
payload['datestamp'] = date_str
r2 = requests.post('http://challenge.code2040.org/api/dating/validate', json = payload)




