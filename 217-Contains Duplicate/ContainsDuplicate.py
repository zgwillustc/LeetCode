def evaluate(function, tests):
    for test in tests:
        actual = function(**test['Input'])
        expect = test['Output']
        print(':', actual == expect)

test0 = {'Input':
                 {'nums': [1,2,3,1]
                  },
         'Output': True
         }

test1 = {'Input':
                 {'nums': [1,2,3,4]
                  },
         'Output': False
         }

test2 = {'Input':
                 {'nums': [1,1,1,3,3,4,3,2,4,2]
                  },
         'Output': True
         }

tests = [test0, test1, test2]

#%% My solution - Memorization - python dictionary - hash table
# Time O(n) Space O(n)
def containsDuplicate(nums) -> bool:
    memo = {}
    for idx, val in enumerate(nums):
        if val in memo:
            return True
        else:
            memo[val] = idx
    return False

evaluate(containsDuplicate, tests)

#%% Brute force - two loops
# Time O(n*n) Space O(1)
def containsDuplicate2(nums) -> bool:
    pass

evaluate(containsDuplicate2, tests)

#%% Sort
# Time O(n*log n) Space O(n)
def containsDuplicate3(nums) -> bool:
    nums.sort()
    for i in range(1,len(nums)):
        if nums[i] == nums[i-1]:
            return True
    return False

evaluate(containsDuplicate3, tests)

#%% Pythonic
# Time O(n) Space O(n)
def containsDuplicate4(nums) -> bool:
    return len(nums) != len(set(nums))

evaluate(containsDuplicate4, tests)
