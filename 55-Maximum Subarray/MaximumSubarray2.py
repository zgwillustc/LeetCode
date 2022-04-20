def evaluate(function, tests):
    for test in tests:
        actual = function(**test['Input'])
        expect = test['Output']
        print(':', actual == expect)

test0 = {'Input':
                 {'nums': [-2,1,-3,4,-1,2,1,-5,4],
                  },
         'Output': 6
         }

test1 = {'Input':
                 {'nums': [1],
                  },
         'Output': 1
         }

test2 = {'Input':
                 {'nums': [5,4,-1,7,8],
                  },
         'Output': 23
         }

test3 = {'Input':
                 {'nums': [-2,1],
                  },
         'Output': 1
         }

tests = [test0, test1, test2, test3]

#%% 
def maxSubArray(nums) -> int:
    maxSum = nums[0]
    curSum = 0
    for n in nums:
        if curSum < 0:
            curSum = 0
        curSum += n
        maxSum = max(curSum, maxSum)
    return maxSum

evaluate(maxSubArray, tests)
