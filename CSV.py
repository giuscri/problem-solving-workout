import functools

def extract_csv(fname):
    '''
    Takes a file name and returns (fields, records)
    '''
    records = []
    with open(fname, 'r') as f:
        lines = f.read().strip().split('\n')
    fields = list(map(lambda x: x.strip(), lines[0].split(';')))
    records = list(map(lambda x: x.split(';'), lines[1:]))
    records = list(map(lambda l: list(map(lambda s: s.strip(), l)), records))
    return fields, records

def pretty_csv(fields, records):
    '''
    Takes (fields, records) representing a csv
    and pretty print the data
    '''
    col_spans = list(map(lambda x: len(x), \
       [functools.reduce(lambda x,y: x if len(x) > len(y) else y, \
       map(lambda x: x[i], records), fields[i]) for i in range(len(fields))])) 
    table_span = sum(col_spans) + 4*len(fields)
    fmts = ['| {{{}:{}}} |'.format(i, x) for i,x in enumerate(col_spans)]
    fmt = ''.join(fmts)
    res = ['-' * table_span, fmt.format(*fields), '-' * table_span]
    res += [fmt.format(*record) for record in records]
    res += ['-' * table_span]
    return '\n'.join(res)

if __name__ == '__main__':
    print(pretty_csv(*extract_csv('languages.csv')))
    print(pretty_csv(*extract_csv('books.csv')))
