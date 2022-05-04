class Solution:
    def reverseBits(self, n: int) -> int:
        # '{0:032b}'.format(n)
        return int(f'{n:b}'.zfill(32)[::-1], 2)

    # Use bit manipulation
    def reverseBits2(self, n: int) -> int:
        ans = 0
        for i in xrange(32):
            ans = (ans << 1) + (n & 1)
            n >>= 1
        return ans

    # https://leetcode.com/problems/reverse-bits/discuss/732138/Python-O(32)-simple-solution-explained
    def reverseBits3(self, n: int) -> int:
        out = 0
        for i in range(32):
            out = (out << 1)^(n & 1)
            n >>= 1
        return out

def evaluate(function, tests):
    for test in tests:
        actual = function(**test['Input'])
        expect = test['Output']
        print('Actual output:', actual)
        print('Expected output:', expect)
        print('Passed?', actual == expect)
        print('\n')

test0 = {'Input':
                 {'n': 43261596
                  },
         'Output': 964176192
         }

test1 = {'Input':
                 {'n': 4294967293
                  },
         'Output': 3221225471
         }

tests = [test0, test1]

def main():
    solution = Solution()
    evaluate(solution.reverseBits, tests)

if __name__ == '__main__':
    main()
