class Solution:
    # My solution
    def hammingWeight(self, n: int) -> int:
        # convert int to binary string
        # "{:b}".format(n)
        # format(n, "b")
        # bin(n)[2:]
        binary_string = f'{n:b}'
        count = 0
        for ch in binary_string:
            if ch == '1':
                count += 1
        return count

    # Inspired by the Discussion
    def hammingWeight2(self, n: int) -> int:
        return bin(n).count('1') # use string method count()

    # Use bit manipulation
    # https://leetcode.com/problems/number-of-1-bits/discuss/1044775/Python-n-and-(n-1)-trick-%2B-even-faster-explained
    def hammingWeight3(self, n: int) -> int:
        # Using bit operation to cancel a 1 in each round
        # Think of a number in binary n = XXXXXX1000, n - 1 is XXXXXX0111.
        # n & (n - 1) will be XXXXXX0000 which is just remove the last significant 1
        c = 0
        while n:
            n &= n - 1
            c += 1
        return c

def evaluate(function, tests):
    for test in tests:
        actual = function(**test['Input'])
        expect = test['Output']
        print('Actual output:', actual)
        print('Expected output:', expect)
        print('Passed?', actual == expect)
        print('\n')

test0 = {'Input':
                 {'n': 11
                  },
         'Output': 3
         }

test1 = {'Input':
                 {'n': 128
                  },
         'Output': 1
         }

test2 = {'Input':
                 {'n': 4294967293
                  },
         'Output': 31
         }

tests = [test0, test1, test2]

def main():
    solution = Solution()
    evaluate(solution.hammingWeight, tests)

if __name__ == '__main__':
    main()
