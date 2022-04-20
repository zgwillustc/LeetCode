def evaluate(function, tests):
    for test in tests:
        actual = function(**test['Input'])
        expect = test['Output']
        print(':', actual == expect)

test0 = {'Input':
                 {'nums': [2,2,1]
                  },
         'Output': 1
         }

test1 = {'Input':
                 {'nums': [4,1,2,1,2]
                  },
         'Output': 4
         }

test2 = {'Input':
                 {'nums': [1]
                  },
         'Output': 1
         }

tests = [test0, test1, test2]

#%% My solution - Python set
# Time O(?) Space O(?)
def singleNumber(nums) -> int:
    return sum(set(nums))*2 - sum(nums)

evaluate(singleNumber, tests)

#%% My solution - Memorization
# Time O(n) Space O(n)
def singleNumber(nums) -> int:
    memo = {}
    for idx, val in enumerate(nums):
        if val in memo:
            memo.pop(val)
        else:
            memo[val] = idx
    return memo.popitem()[0]

evaluate(singleNumber, tests)

#%% Discussion
# Hashing
def singleNumber1(self, nums):
    dic = {}
    for num in nums:
        dic[num] = dic.get(num, 0)+1
    for key, val in dic.items():
        if val == 1:
            return key
# Xor/Bit Manipulation
# Time O(n) Space O(1)
def singleNumber2(self, nums):
    res = 0
    for num in nums:
        res ^= num
    return res
# reduce
def singleNumber3(self, nums):
    return reduce(lambda x, y: x ^ y, nums)

def singleNumber(self, nums):
    return reduce(operator.xor, nums)
