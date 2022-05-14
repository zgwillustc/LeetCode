'''
Given an integer n, return an array ans of length n + 1 such that for each i
(0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
'''
from typing import List

class Solution:
    # My solution
    def countBits2(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            binary_string = format(i, 'b')
            ans.append(binary_string.count('1'))
        return ans

# https://leetcode.com/problems/counting-bits/discuss/656849/Python-Simple-Solution-with-Clear-Explanation

    # Brute force
    # Time O(n log n)

    # Dynamic programming
    # Time O(n)
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        offset = 1
        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp

def evaluate(function, tests):
    for test in tests:
        actual = function(**test['Input'])
        expect = test['Output']
        print('Actual output:', actual)
        print('Expected output:', expect)
        print('Passed?', actual == expect)
        print('\n')

test0 = {'Input':
                 {'n': 2
                  },
         'Output': [0,1,1]
         }

test1 = {'Input':
                 {'n': 5
                  },
         'Output': [0,1,1,2,1,2]
         }

test2 = {'Input':
                 {'n': 0
                  },
         'Output': [0]
         }

tests = [test0, test1, test2]

def main():
    solution = Solution()
    evaluate(solution.countBits, tests)

if __name__ == '__main__':
    main()
