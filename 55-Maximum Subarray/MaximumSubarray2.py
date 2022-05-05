'''
Given an integer array nums, find the contiguous subarray
(containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.
'''

class Solution:
    def maxSubArray2(self, nums: list) -> int:
        maxSub = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub

    # Dynamic programming
    def maxSubArray3(self, nums: list) -> int:
        maxSub = nums[0]
        dp = [maxSub] * len(nums)
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i-1])
            maxSub = max(dp[i], maxSub)
        return maxSub

    def maxSubArray(self, nums: list) -> int:
        maxSub = max_ending_here = nums[0]
        for i in range(1, len(nums)):
            max_ending_here = max(nums[i], nums[i] + max_ending_here)
            maxSub = max(max_ending_here, maxSub)
        return maxSub


def evaluate(function, tests):
    for test in tests:
        actual = function(**test['Input'])
        expect = test['Output']
        print('Actual output:', actual)
        print('Expected output:', expect)
        print('Passed?', actual == expect)
        print('\n')

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
                 {'nums': [-5,-1,-2],
                  },
         'Output': -1
         }

test4 = {'Input':
                 {'nums': [1,2],
                  },
         'Output': 3
         }

test5 = {'Input':
                 {'nums': [8,-19,5,-4,20],
                  },
         'Output': 21
         }

tests = [test0, test1, test2, test3, test4, test5]

def main():
    solution = Solution()
    evaluate(solution.maxSubArray, tests)

if __name__ == '__main__':
    main()
