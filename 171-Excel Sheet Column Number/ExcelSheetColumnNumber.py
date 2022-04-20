def evaluate(function, tests):
    for test in tests:
        actual = function(**test['Input'])
        expect = test['Output']
        print('Result:', actual == expect)

test0 = {'Input': 
                 {'columnTitle': "A",
                  },
         'Output': 1
         }

test1 = {'Input': 
                 {'columnTitle': "AB",
                  },
         'Output': 28
         }

test2 = {'Input': 
                 {'columnTitle': 'ZY',
                  },
         'Output': 701
         }

tests = [test0, test1, test2]

#%% My solution - need a self-built mapping
trans = {}
alphabet_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for idx, s in enumerate(alphabet_string):
    trans[s] = idx + 1

def titleToNumber(columnTitle: str) -> int:
    num = 0
    length = len(columnTitle)
    for idx, s in enumerate(columnTitle):
        num += trans[s] * 26**(length - idx - 1)
    return num

evaluate(titleToNumber, tests)

#%% Inspired by the Discussion
# use python built-in function: ord() & reversed()
# chr() works oppositely to ord()
def titleToNumber2(columnTitle: str) -> int:
    num = 0
    for idx, s in enumerate(reversed(columnTitle)):
        num += (ord(s) - 64) * 26**idx
    return num
        
evaluate(titleToNumber2, tests)



