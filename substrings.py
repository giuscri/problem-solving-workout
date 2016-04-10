def find_substrings(s):
    lst = [set(s[i]) for i in range(len(s))]

    for i in range(1, len(s)):
        for x in lst[i-1]:
            lst[i].add(x + s[i])

    ret = ['']
    for x in lst:
        for y in x:
            ret.append(y)

    return ret 

if __name__ == '__main__':
    import string

    print(find_substrings(string.printable[10:10+26]))
