import re
import unittest

def is_palindrome(s):
    s = ''.join(re.findall('\w+', s)).lower()
    lst1 = list(s)
    lst2 = lst1[:]
    lst2.reverse()
    ret = True
    for x,y in zip(lst1, lst2):
        if x != y:
            ret = False
    return ret

def is_valid_tictactoe(s):
    '''
    Returns the result as (<Valid match>, <Even match>, <X won>, <O won>)
    '''
    res = {
        'is_valid_match': False,
        'is_even_match': False,
        'X_won': False,
        'O_won': False
    }

    if len(s) != 9: return res

    if s.count('X') == s.count('O')-1 \
     or s.count('X') == s.count('O')+1 \
     or s.count('X') == s.count('O'):
        res['is_valid_match']=True
    else:
        return res

    winning_configurations = []
    winning_configurations.extend([{(x,y) for y in range(3)} for x in range(3)])
    winning_configurations.extend([{(y,x) for y in range(3)} for x in range(3)])
    winning_configurations.append({(x,x) for x in range(3)})
    winning_configurations.append({(0,2), (1,1), (2,0)})

    m = [[s[i] for i in range(0,3)], [s[i] for i in range(3,6)], [s[i] for i in range(6,9)]]

    X_positions = set()
    
    for i in range(0,3):
        for j in range(0,3):
            if m[i][j] == 'X':
                X_positions.add((i,j))

    if X_positions in winning_configurations:
        res['X_won'] = True
        return res

    O_positions = set()
    
    for i in range(0,3):
        for j in range(0,3):
            if m[i][j] == 'O':
                O_positions.add((i,j))

    if O_positions in winning_configurations:
        res['O_won'] = True
        return res

    if not res['X_won'] and not res['O_won'] and s.count(' ')<=1:
        res['is_even_match'] = True
        return res

    return res

class MainTest(unittest.TestCase):

    def test_is_palindrome(self):
        lst = (
            'Rise to vote, sir.',
            'Do geese see God?',
            'detartrated',
            'purple h4ze'
        )
        results = (True, True, True, False)
        for x, y in zip(lst, results):
            self.assertEqual(is_palindrome(x), y)

    def test_is_valid_tictactoe(self):
        lst = (
            '',
            'X O',
            'O XO X  X',
            'X O OXO  ',
            'XO OXXOXO',
            'XOXOXXOXO',
        )
        results = (
            {'is_valid_match': False, 'is_even_match': False, 'X_won': False, 'O_won': False},
            {'is_valid_match': False, 'is_even_match': False, 'X_won': False, 'O_won': False},
            {'is_valid_match': True,  'is_even_match': False, 'X_won': True,  'O_won': False},
            {'is_valid_match': True,  'is_even_match': False, 'X_won': False, 'O_won': True},
            {'is_valid_match': True,  'is_even_match': True, 'X_won': False,  'O_won': False},
            {'is_valid_match': True,  'is_even_match': True,  'X_won': False, 'O_won': False},
        )
        for x,y in zip(lst, results):
            self.assertEqual(is_valid_tictactoe(x), y)

if __name__ == '__main__':
    unittest.main()
