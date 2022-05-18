'''
Given an integer array nums of size n, return the number with the value closest
to 0 in nums. If there are multiple answers, return the number with the largest
value.

Constraints:
1 <= n <= 1000
-10^5 <= nums[i] <= 10^5
'''
from typing import List

class Solution:
    # My Solution
    # Time O(n) Space O(1)
    def findClosestNumber1(self, nums: List[int]) -> int:
        closestToZero = float('inf')
        for num in nums:
            if abs(num) < abs(closestToZero):
                closestToZero = num
            elif abs(num) == abs(closestToZero):
                closestToZero = max(num, closestToZero)
        return closestToZero

def evaluate(function, tests):
    for test in tests:
        actual = function(**test['Input'])
        expect = test['Output']
        print('Actual output:', actual)
        print('Expected output:', expect)
        print('Passed?', actual == expect)
        print('\n')

test0 = {'Input':
                 {'nums': [-4,-2,1,4,8]
                  },
         'Output': 1
         }

test1 = {'Input':
                 {'nums': [2,-1,1]
                  },
         'Output': 1
         }

test2 = {'Input':
                 {'nums': [2,-1,-2]
                  },
         'Output': -1
         }

tests = [test0, test1, test2]

def main():
    solution = Solution()
    evaluate(solution.findClosestNumber, tests)

if __name__ == '__main__':
    main()
