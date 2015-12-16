import re
import unittest

def build_match_and_apply_functions(pattern, search, replace):
    match_function = lambda noun: re.search(pattern, noun)
    apply_function = lambda noun: re.sub(search, replace, noun)
    return match_function, apply_function

'''
def rules(fname):
    with open(fname) as f:
        for line in f.readlines():
            pattern = re.split('\s+', line.strip())
            yield build_match_and_apply_functions(*pattern)
'''

class LazyRules:
    def __init__(self, rules_filename):
        self.rules_file = open(rules_filename, encoding='utf-8')
        self.cache = []
    def __iter__(self):
        self.cache_index = 0
        return self
    def __next__(self):
        self.cache_index +=1
        if len(self.cache) >= self.cache_index:
            return self.cache[self.cache_index - 1]
        if self.rules_file.closed: raise StopIteration
        line = self.rules_file.readline()
        if not line:
            self.rules_file.close()
            raise StopIteration
        funcs = build_match_and_apply_functions(*re.split('\s+', line.strip()))
        self.cache.append(funcs)
        return funcs

rules = LazyRules('rules')

def pluralize(noun):
    for matches_rule, apply_rule in rules:
        if matches_rule(noun):
            return apply_rule(noun)
    raise ValueError('No matching rule for {}'.format(noun)) 

class MainTest(unittest.TestCase):
    def test_pluralize(self):
        self.assertEqual(pluralize('fax'), 'faxes')
        self.assertEqual(pluralize('coach'), 'coaches')
        self.assertEqual(pluralize('vacancy'), 'vacancies')
        self.assertEqual(pluralize('foobar'), 'foobars')

if __name__ == '__main__':
    unittest.main()
