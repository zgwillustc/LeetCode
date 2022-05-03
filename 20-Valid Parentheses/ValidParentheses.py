class Solution:
    # My solution - stack
    # Time O(n) Space O(1) but too many if statements
    def isValid(self, s: str) -> bool:
        stack = []
        left = {'(', '[', '{'}
        right = {')', ']', '}'}
        for ch in s:
            if ch in left:
                stack.append(ch)
            if ch in right:
                if not stack:
                    return False
                temp = stack.pop()
                if temp == '(' and ch != ')' or \
                   temp == '[' and ch != ']' or \
                   temp == '{' and ch != '}':
                    return False
        return not stack

    # Use stack and hash map
    def isValid2(self, s: str) -> bool:
#        if len(s)%2!=0:
#            return False

        stack = []
        brackets = {'(': ')', '[': ']', '{': '}'}
        for ch in s:
            if ch in brackets:
                stack.append(ch)
            elif not stack or brackets[stack.pop()] != ch:
                return False
        return not stack


def evaluate(function, tests):
    for test in tests:
        actual = function(**test['Input'])
        expect = test['Output']
        print('Actual output:', actual)
        print('Expected output:', expect)
        print('Passed?', actual == expect)
        print('\n')

test0 = {'Input':
                 {'s': "()"
                  },
         'Output': True
         }

test1 = {'Input':
                 {'s': "()[]{}"
                  },
         'Output': True
         }

test2 = {'Input':
                 {'s': "(])"
                  },
         'Output': False
         }

tests = [test0, test1, test2]

def main():
    solution = Solution()
    evaluate(solution.isValid, tests)

if __name__ == '__main__':
    main()
