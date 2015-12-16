import itertools
import math

def recover_ip_str(mangled_str):
    '''
    Given a mangled ip string, compute
    all the possible original ip strings.
    '''
    recovered = []
    combs = itertools.combinations(range(len(mangled_str) +1), 5)
    # Make sure that any resulting candidate comprises
    # all the digits of the mangled string
    combs = filter(lambda x: x[0]==0 and x[-1]==len(mangled_str), combs)
    for comb in combs:
        valid_ip_str = True
        ip_str = ''
        for i in range(4):
            if len(mangled_str[comb[i]:comb[i+1]]) > 4:
                valid_ip_str = False
                break
            if int(mangled_str[comb[i]:comb[i+1]]) > 255:
                valid_ip_str = False
                break
            ip_str += mangled_str[comb[i]:comb[i+1]]
            ip_str += '.'
        if valid_ip_str:
            recovered.append(ip_str[:-1])
    return recovered

# A less pythonic way of doing the same
def _recover_ip_str(mangled_str):
    '''
    Given a mangled ip string, compute
    all the possible original ip strings.
    '''
    recovered = []
    for first_dot in range(1, math.ceil(len(mangled_str)/4) +1):
        if int(mangled_str[0:first_dot]) > 255:
            break
        for second_dot in range(first_dot +1, first_dot +4):
            if int(mangled_str[first_dot:second_dot]) > 255:
                break
            for third_dot in range(second_dot +1, second_dot +4):
                if int(mangled_str[second_dot:third_dot]) > 255:
                    break
                if mangled_str[third_dot:] == '':
                    break
                if int(mangled_str[third_dot:]) > 255:
                    continue
                ip_str = mangled_str[0:first_dot] + '.'
                ip_str += mangled_str[first_dot:second_dot] + '.'
                ip_str += mangled_str[second_dot:third_dot] + '.'
                ip_str += mangled_str[third_dot:]
                if len(ip_str) == len(mangled_str) +3:
                    recovered.append(ip_str)
    return recovered

if __name__ == '__main__':
    assert '192.168.11.22' in _recover_ip_str('1921681122')

