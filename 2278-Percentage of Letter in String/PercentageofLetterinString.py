'''
Given a string s and a character letter, return the percentage of characters in
s that equal letter rounded down to the nearest whole percent.

Constraints:
1 <= s.length <= 100
s consists of lowercase English letters.
letter is a lowercase English letter.
'''
class Solution:
    # Time O(n) Space O(1)
    def percentageLetter1(self, s: str, letter: str) -> int:
        num = 0
        for char in s:
            if char == letter:
                num += 1
        return int( num / len(s) * 100 )

    def percentageLetter(self, s: str, letter: str) -> int:
        return s.count(letter) * 100 // len(s)


def evaluate(function, tests):
    for test in tests:
        actual = function(**test['Input'])
        expect = test['Output']
        print('Actual output:', actual)
        print('Expected output:', expect)
        print('Passed?', actual == expect)
        print('\n')

test0 = {'Input':
                 {'s': 'foobar',
                  'letter': 'o'
                  },
         'Output': 33
         }

test1 = {'Input':
                 {'s': 'jjjj',
                  'letter': 'k'
                  },
         'Output': 0
         }

test2 = {'Input':
                 {'s': 'l',
                  'letter': 'l'
                  },
         'Output': 100
         }

tests = [test0, test1, test2]

def main():
    solution = Solution()
    evaluate(solution.percentageLetter, tests)

if __name__ == '__main__':
    main()
