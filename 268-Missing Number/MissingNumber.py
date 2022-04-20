def evaluate(function, tests):
    for test in tests:
        actual = function(**test['Input'])
        expect = test['Output']
        print(':', actual == expect)

test0 = {'Input': 
                 {'nums': [3,0,1]
                  },
         'Output': 2
         }

test1 = {'Input': 
                 {'nums': [0,1]
                  },
         'Output': 2
         }

test2 = {'Input': 
                 {'nums': [9,6,4,2,3,5,7,0,1]
                  },
         'Output': 8
         }

tests = [test0, test1, test2]

#%% My solution
def missingNumber(nums) -> int:
    return sum(range(len(nums)+1)) - sum(nums)

evaluate(missingNumber, tests)

#%% Brute force
def missingNumber2(nums) -> int:
    memo = list(range(len(nums)+1))
    for i in nums:
        memo.remove(i)
    return memo[0]

evaluate(missingNumber2, tests)

#%% Use only one sum() function
def missingNumber3(nums):
    n = len(nums)
    return n * (n+1) / 2 - sum(nums)
