'''
Given a non-negative integer x, compute and return the square root of x.
Since the return type is an integer, the decimal digits are truncated, and only
the integer part of the result is returned.
Note: You are not allowed to use any built-in exponent function or operator,
such as pow(x, 0.5) or x ** 0.5.

Example 1:
Input: x = 4
Output: 2

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is
truncated, 2 is returned.

Constraints:
0 <= x <= 231 - 1
'''
class Solution:
    # My solution - Iteration
    # Time O(sqrt(n)) Space O(1)
    def mySqrt(self, x: int) -> int:
        sqrt = 0
        while sqrt*sqrt <= x:
            sqrt += 1
        return sqrt - 1

    # Use the idea of binary search.
    # https://leetcode.com/problems/sqrtx/discuss/344755/Python-solution-with-binary-search
    # Time O(log n) Space O(1)
    def mySqrt2(self, x: int) -> int:
        left, right = 0, x
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid <= x <= (mid+1) * (mid+1):
                return mid
            elif x < mid * mid:
                right = mid - 1
            else:
                left = mid + 1

    # Newton's method - root finding
    # https://leetcode.com/problems/sqrtx/discuss/359172/Python-Newton-Solution
    # Time O(log n) Space O(1)
    def mySqrt3(self, x: int) -> int:
        res = x
        while res * res > x:
            res = int((res + x/res) / 2)
        return res

    # Bit manipulation
    # Time O(log n)

def evaluate(function, tests):
    for test in tests:
        actual = function(**test['Input'])
        expect = test['Output']
        print('Actual output:', actual)
        print('Expected output:', expect)
        print('Passed?', actual == expect)
        print('\n')

test0 = {'Input':
                 {'x': 4
                  },
         'Output': 2
         }

test1 = {'Input':
                 {'x': 8
                  },
         'Output': 2
         }

test2 = {'Input':
                 {'x': 0
                  },
         'Output': 0
         }

tests = [test0, test1, test2]

def main():
    solution = Solution()
    evaluate(solution.mySqrt2, tests)

if __name__ == '__main__':
    main()
