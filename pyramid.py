def pyramid(height=42):
    '''
    Prints stuff like this

        *
       ***
      *****
     *******
    *********
    '''
    ret = []
    for nstars in range(1,height,2):
        nspaces = height - nstars
        ret.append(' ' * (nspaces//2) + '*' * nstars + ' ' * (nspaces//2))
    return '\n'.join(ret)

if __name__ == '__main__':
    print(pyramid())
