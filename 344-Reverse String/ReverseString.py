def evaluate(function, tests):
    for test in tests:
        actual = function(**test['Input'])
        expect = test['Output']
        print(':', actual == expect)

test0 = {'Input': 
                 {'s': ["h","e","l","l","o"],
                  },
         'Output': ["o","l","l","e","h"]
         }

test1 = {'Input': 
                 {'s': ["H","a","n","n","a","h"],
                  },
         'Output': ["h","a","n","n","a","H"]
         }

test2 = {'Input': 
                 {'s': ['m'],
                  },
         'Output': ['m']
         }

tests = [test0, test1, test2]

#%%
# Use Python list methods
def reverseString(s):
    for i in range(len(s)):
        s.insert(i, s.pop())
    # or use Python list reverse() method
    # s[:] = [::-1]

# Two pointer solution - inspired by the hint
def reverseString2(s):
    i, j = 0, len(s)-1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1

# Mirror image    
    # for i in range(len(s)//2): 
    #     s[i], s[-i-1] = s[-i-1], s[i]
    #     # s[i], s[~i] = s[~i], s[i]

# Recursion solution
def reverseString3(s):
    def helper(left, right, string):     
            
        if left >= right:
            # base case
            return
        
        # general case
        s[left], s[right] = s[right], s[left]
        
        helper( left+1, right-1, s)
    # ------------------------------------------------
    
    helper( left = 0, right = len(s)-1, string = s)


