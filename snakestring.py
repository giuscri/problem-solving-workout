def snake_string(s):
    tokens = []
    tokens += ''.join(map(lambda p: p[1], filter(lambda x: x[0]%4==1, enumerate(s))))
    tokens += ''.join(map(lambda p: p[1], filter(lambda x: x[0]%4==0 or x[0]%4==2, enumerate(s))))
    tokens += ''.join(map(lambda p: p[1], filter(lambda x: x[0]%4==3, enumerate(s))))
    return ''.join(tokens)

if __name__ == '__main__':
    assert snake_string('Hello World!') == 'e lHloWrdlo!'
