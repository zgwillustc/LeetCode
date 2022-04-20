def evaluate(function, tests):
    for test in tests:
        actual = function(**test['Input'])
        expect = test['Output']
        print('Result:', actual == expect)

test0 = {'Input': 
                 {'columnNumber': 1,
                  },
         'Output': 'A'
         }

test1 = {'Input': 
                 {'columnNumber': 28,
                  },
         'Output': 'AB'
         }

test2 = {'Input': 
                 {'columnNumber': 701,
                  },
         'Output': 'ZY'
         }

tests = [test0, test1, test2]

#%% Inspired by the discussion
# Note that excel number system starts from 1 instead of 0
# Compare to 10-base numerical system
def convertToTitle(columnNumber: int) -> str:
    res = ''
    while columnNumber:
        columnNumber -= 1 # Important
        res = chr(columnNumber % 26 + ord('A')) + res
        columnNumber = columnNumber // 26
    return res
            
evaluate(convertToTitle, tests)

