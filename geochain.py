def chain(source):
    countries = (   
        'portugal',
        'spain',
        'france',
        'luxembourg',
        'belgium',
        'netherlands',
        'denmark',
        'germany',
        'norway',
        'sweden',
        'finland',
        'estonia',
        'lithuania',
        'latvia',
        'belarus',
        'poland',
        'czech republic',
        'slovakia',
        'hungary',
        'austria',
        'switzerland',
        'italy',
        'hungary',
        'romania',
        'serbia',
        'bulgaria',
        'macedonia',
        'greece',
        'albania',
        'montenegro',
        'bosnia and herzegovina'
        'croatia',
        'slovenia',
        'moldova',
        'ukraine',
        'russia',
        'andorra',
        'liechtenstein',
    )

    def _chain(source, cn, cns):
        cs = [c for c in countries \
                 if source[-1]==c[0] and \
                       c not in cn]

        if len(cs)==0:
            cns.append(cn)
            return cns

        for c in cs:
            _chain(c, cn + [c], cns)

        return cns

    cns = _chain(source, [source], [])

    ## Group chains by len, so that we have
    ##
    ##   [([[<chain>], [<chain>], ...]], <len>), ...]
    lst = [(c,len(c)) for c in cns]
    lst = [([q[0] for q in lst if q[1]==p[1]], p[1]) for p in lst]

    ## Sort the list by len, descending
    lst.sort(key=lambda p: p[1], reverse=True)

    ## Take the group of longest chains, and
    ## take the chains only
    lst = lst[0][0]

    ## Sort it by lexicographical order, ascending
    lst.sort()

    ## Return the first one
    return lst[0]

if __name__ == '__main__':
    print("the longest chain starting from {0} is {1}".
    format('italy', chain('italy')))
    print("the longest chain starting from {0} is {1}".
    format('spain', chain('spain')))
    print("the longest chain starting from {0} is {1}".
    format('switzerland', chain('switzerland')))
    print("the longest chain starting from {0} is {1}".
    format('luxembourg', chain('luxembourg')))
    print("the longest chain starting from {0} is {1}".
    format('belarus', chain('belarus')))
    print("the longest chain starting from {0} is {1}".
    format('belgium', chain('belgium')))
    print("the longest chain starting from {0} is {1}".
    format('portugal', chain('portugal')))
