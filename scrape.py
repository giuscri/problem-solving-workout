import requests
import threading
import functools

url_fmt = 'http://cazzola.di.unimi.it/didattica/programmazione-avanzata/esame-{0}-{1:02}-{2:02}.html'

def f(r_y, r_m, r_d, OK_urls, lk):
    for y in r_y:
        for m in r_m:
            for d in r_d:
                url = url_fmt.format(y, m, d)
                #print('[-] Trying {} ...'.format(url))
                r = requests.get(url, auth=('pa', 'PA+#2009#'))
                if r.status_code == 200:
                    print('[+] Gotcha!, {}'.format(url))
                    OK_urls.append(url)

    with lk: lk.notify()

ts = []
OK_urls = []
lk = threading.Condition()

for i in range(8):
    args = (
        range(2008 + i, 2009 + i),
        range(1,12),
        range(1,31),
        OK_urls,
        lk,
    )
    ts.append(threading.Thread(target=f, args=args))

for t in ts:
    t.start()

with lk:
    all_done = lambda ts=ts: \
                  not functools.reduce(lambda x,y: x or y, \
                                          [t.is_alive() for t in ts])
    lk.wait_for(all_done)

print(OK_urls)

with open('OK_urls.txt', 'w') as f:
    for url in OK_urls:
        f.write(url + '\n')
