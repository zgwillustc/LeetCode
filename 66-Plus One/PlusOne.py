def evaluate(function, tests):
    for test in tests:
        actual = function(**test['Input'])
        expect = test['Output']
        print(':', actual == expect)

test0 = {'Input': 
                 {'digits': [1,2,3],
                  },
         'Output': [1,2,4]
         }

test1 = {'Input': 
                 {'digits': [4,3,2,1],
                  },
         'Output': [4,3,2,2]
         }

test2 = {'Input': 
                 {'digits': [9],
                  },
         'Output': [1,0]
         }

tests = [test0, test1, test2]

#%% My solution
def plusOne(digits):
    for i in range(len(digits)-1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            break
        else:
            digits[i] = 0
    if digits[0] == 0:
        digits = [1] + digits
    return digits

evaluate(plusOne, tests)

# There is some other solutions based on math

#%% Recursion
# inspired by Discussion


