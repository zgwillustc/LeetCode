'''
Given two strings s and t, return true if they are equal when both are typed
into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Constraints:
1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.

Follow up: Can you solve it in O(n) time and O(1) space?
'''
class Solution:
    # My solution
    # Time O(m+n)
    # Space O(m+n)
    def backspaceCompare2(self, s: str, t: str) -> bool:

        def string2Stack(s):
            stack = []
            for ch in s:
                if ch == '#' and stack:
                    stack.pop()
                elif ch != '#':
                    stack.append(ch)
            return stack

        s_stack = string2Stack(s)
        t_stack = string2Stack(t)
        return s_stack == t_stack

# Inspired by solution
# Build string - similar to my Solution
# Time O(m+n) Space O(m+n)
    def backspaceCompare3(self, s: str, t: str) -> bool:
        def build(S):
            ans = []
            for c in S:
                if c != '#':
                    ans.append(c)
                elif ans:
                    ans.pop()
            return "".join(ans)
        return build(s) == build(t)

# Two pointers
# Time O(m+n) Space O(1)
    def backspaceCompare(self, s: str, t: str) -> bool:
        r1 = len(s) - 1
        r2 = len(t) - 1

        while r1 >= 0 or r2 >= 0:
            char1 = char2 = ""
            if r1 >= 0:
                char1, r1 = self.getChar(s, r1)
            if r2 >= 0:
                char2, r2 = self.getChar(t, r2)
            if char1 != char2:
                return False
        return True

    def getChar(self, s , r):
        char, count = '', 0
        while r >= 0 and not char:
            if s[r] == '#':
                count += 1
            elif count == 0:
                char = s[r]
            else:
                count -= 1
            r -= 1
        return char, r

def evaluate(function, tests):
    for test in tests:
        actual = function(**test['Input'])
        expect = test['Output']
        print('Actual output:', actual)
        print('Expected output:', expect)
        print('Passed?', actual == expect)
        print('\n')

test0 = {'Input':
                 {'s': 'ab#c',
                  't': 'ad#c'
                  },
         'Output': True
         }

test1 = {'Input':
                 {'s': 'ab##',
                  't': 'c#d#'
                  },
         'Output': True
         }

test2 = {'Input':
                 {'s': 'a#c',
                  't': 'b'
                  },
         'Output': False
         }

test3 = {'Input':
                 {'s': 'a',
                  't': 'aa#'
                  },
         'Output': True
         }

test4 = {'Input':
                 {'s': 's##',
                  't': 'c#'
                  },
         'Output': True
         }

tests = [test0, test1, test2, test3, test4]

def main():
    solution = Solution()
    evaluate(solution.backspaceCompare, tests)

if __name__ == '__main__':
    main()
