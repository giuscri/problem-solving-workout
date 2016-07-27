if __name__ == '__main__':
	encrypted = b'5Gr8L4qetPEsPk8htqjhRK8XSP6x2RHh'

	def fn(n):
		if n <= 0x5A:
			return ((n - 0x41 + 13) % 26) + 0x41
		else:
			return ((n - 0x61 + 13) % 26) + 0x61

	decrypted = \
		bytes(map(lambda n: n if n in range(0x30, 0x3A) else fn(n), encrypted))

	print(decrypted)
