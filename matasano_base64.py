import binascii

def hex2base64(hex_str):
    input_bytes = binascii.unhexlify(hex_str)
    output_bytes = bytearray()

    for i in range(0, len(input_bytes), 3):
        output_bytes.append(input_bytes[i] >> 2)
        output_bytes.append((input_bytes[i] << 4) & 0x3f | input_bytes[i+1] >> 4)
        output_bytes.append((input_bytes[i+1] << 2) & 0x3f| input_bytes[i+2] >> 6)
        output_bytes.append(input_bytes[i+2] & 0x3f)

    alphabet = [chr(x) for x in range(ord('A'), ord('Z') +1)]
    alphabet.extend([chr(x) for x in range(ord('a'), ord('z') +1)])
    alphabet.extend([chr(x) for x in range(ord('0'), ord('9') +1)])
    alphabet.extend(['+', '/'])

    return ''.join(map(lambda x: alphabet[x], output_bytes))

if __name__ == '__main__':
    assert hex2base64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d') \
    == 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
