class Solution:
    # My solution - recursion
    # Time O(log3 n) Space O(log3 n)
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        q, r = divmod(n, 3)
        if r != 0 or n == 0:
            return False
        return self.isPowerOfThree(q)

    # My solution - iteration
    # Time O(log3 n) Space O(1)
    def isPowerOfThree2(self, n: int) -> bool:
        test = 1
        while test < n:
            test *=3
        return test == n

#        if n < 1:
#            return False
#        while n % 3 == 0:
#            n /= 3
#        return n == 1

    # https://leetcode.com/problems/power-of-three/solution/
    # Time O(1) Space O(1)
    def isPowerOfThree3(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0

def evaluate(function, tests):
    for test in tests:
        actual = function(**test['Input'])
        expect = test['Output']
        print('Actual output:', actual)
        print('Expected output:', expect)
        print('Passed?', actual == expect)
        print('\n')

test0 = {'Input':
                 {'n': 27
                  },
         'Output': True
         }

test1 = {'Input':
                 {'n': 0
                  },
         'Output': False
         }

test2 = {'Input':
                 {'n': 1
                  },
         'Output': True
         }

tests = [test0, test1, test2]

def main():
    solution = Solution()
    evaluate(solution.isPowerOfThree, tests)

if __name__ == '__main__':
    main()
