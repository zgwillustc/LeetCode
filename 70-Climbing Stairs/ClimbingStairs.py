'''
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
1 <= n <= 45
'''
class Solution:
    # This problem is essentially Fibonacci sequence
    # f(n) = f(n-1) + f(n-2)

    # My solution
    # Recursion - Exceed time limit on LeetCode
    # There are overlapping subproblems
    # Time O(2^n) Space O(log n) ?
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)

    # Dynamic programming - memorization - top down
    # Time O(n) Space O(n)
    def climbStairs2(self, n: int) -> int:
        m = [i for i in range(n+1)]
        for i in range(3, n+1):
            m[i] = m[i-1] + m[i-2]
        return m[n]

    # Dynamic programming - bottom up
    # Time O(n) Space O(1)
    def climbStairs3(self, n: int) -> int:
        if n <= 2:
            return n
        prev = 1; curr = 2
        for i in range(n-2):
            new = prev + curr
            prev, curr = curr, new
        return new

        # Another bottom up
#        a = b = 1
#        for _ in range(n):
#            a, b = b, a + b
#        return a

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
         'Output': 2
         }

test1 = {'Input':
                 {'n': 3
                  },
         'Output': 3
         }

test2 = {'Input':
                 {'n': 5
                  },
         'Output': 8
         }

tests = [test0, test1, test2]

def main():
    solution = Solution()
    evaluate(solution.climbStairs3, tests)

if __name__ == '__main__':
    main()
