'''
Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.
For example, 121 is a palindrome while 123 is not.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it
becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:
-231 <= x <= 231 - 1

Follow up: Could you solve it without converting the integer to a string?
'''
class Solution:
    # My solution
    # convert to string, two pointers
    # Time O(n) Space O(n)
    def isPalindrome2(self, x: int) -> bool:
        str_x = str(x)
        l, r = 0, len(str_x)-1
        while l < r:
            if str_x[l] != str_x[r]:
                return False
            l += 1
            r -= 1
        return True

    # Pythonic Solution
    # return str(x) == str(x)[::-1]

    # Inspired by the Solution - Revert half of the number
    # Negative numbers are not palindrome
    # % 10 gives the last digit; // 10 removes last digit
    def isPalindrome3(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        revert = 0
        while x > revert:
            revert = revert * 10 + x % 10
            x //= 10
        print(x, revert)

        return x == revert or x == revert // 10

    # Inspired by the Discussion - Revert the whole number
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        quotient, revert = x, 0
        while quotient:
            revert = revert * 10 + quotient % 10
            quotient //= 10
        return x == revert

def evaluate(function, tests):
    for test in tests:
        actual = function(**test['Input'])
        expect = test['Output']
        print('Actual output:', actual)
        print('Expected output:', expect)
        print('Passed?', actual == expect)
        print('\n')

test0 = {'Input':
                 {'x': 121
                  },
         'Output': True
         }

test1 = {'Input':
                 {'x': -121
                  },
         'Output': False
         }

test2 = {'Input':
                 {'x': 10
                  },
         'Output': False
         }

tests = [test0, test1, test2]

def main():
    solution = Solution()
    evaluate(solution.isPalindrome, tests)

if __name__ == '__main__':
    main()
