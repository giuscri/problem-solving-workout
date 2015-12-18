class C(object):
    '''
    def __getattr__(self, attribute):
        return 'What the fuck?!'
    '''
    def __getattribute__(self, attribute):
        print('What the ****?!')
        try:
            return object.__getattribute__(self, attribute)
        except AttributeError: pass

    foo = 42
