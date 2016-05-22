import base64

with open('data.txt') as f:
    base64.b64decode(f.readline().strip()).decode('UTF-8')
