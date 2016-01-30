import string

kys = string.printable[10+26:10+26*2] + \
         string.printable[10:10+26] + \
            string.printable[:10] + '+/'
mp = dict(zip(kys, range(0, 64)))
mp['='] = 0

def unb64(s):
    r = [] 
    for i in range(0, len(s), 4):
        r.append((mp[s[i]] << 2 | mp[s[i+1]] >> 4) & 0xff)
        r.append((mp[s[i+1]] << 4 | mp[s[i+2]] >> 2) & 0xff)
        r.append((mp[s[i+2]] << 6 | mp[s[i+3]]) & 0xff)
    npd = s.count('=')
    if npd > 0: r = r[:-npd]
    return r

if __name__ == '__main__':
    assert bytes(unb64('Rm9vYmFyaXNtIGlzIHRoZSB3YXk=')) == b'Foobarism is the way'
