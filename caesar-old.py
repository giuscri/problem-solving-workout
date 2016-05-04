class caesar_cipher:
    def __init__(self, e_key):
        self.e_key = e_key
        self.d_key = 26-e_key

    def encrypt(self, s):
        s = s.lower()
        lst = []
        for c in s:
            if c != ' ':
                lst.append(chr((ord(c)-ord('a') +self.e_key) % 26 + ord('a')))
            else:
                lst.append(c)
        return ''.join(lst)

    def decrypt(self, s):
        s = s.lower()
        lst = []
        for c in s:
            if c != ' ':
                lst.append(chr((ord(c)-ord('a') +self.d_key) % 26 + ord('a')))
            else:
                lst.append(c)
        return ''.join(lst)
