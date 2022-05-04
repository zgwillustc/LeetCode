'''
Implement strStr().
Given two strings needle and haystack, return the index of the first occurrence
of needle in haystack, or -1 if needle is not part of haystack.

Clarification:
What should we return when needle is an empty string? This is a great question
to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string.
This is consistent to C's strstr() and Java's indexOf().

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Constraints:
1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
'''
class Solution:
    # My solution - two pointers
    # Time O(m * n) Space O(m * n)?string slicing uses extra space
    def strStr(self, haystack: str, needle: str) -> int:
        left, right = 0, len(needle)
        while right <= len(haystack):
            if haystack[left:right] == needle: # string comparison is O(n)
                return left
            left += 1
            right += 1
        return -1

    # KMP algorithm
    # Time O(m * n) Space O(m)
    # First of all, we generate the "next" array to show any possible duplicates
    # of prefix and postfix within needle. Then we go through haystack.
    # Every time we see a bad match, move j to next[j] and keep i in current position;
    # otherwise, move both of them to next position.
    def strStr2(self, haystack: str, needle: str) -> int:
        if haystack == None or needle == None:
            return -1
        #generate next array, need O(n) time
        i, j, m, n = -1, 0, len(haystack), len(needle)
        next = [-1] * n
        while j < n - 1:
            #needle[k] stands for prefix, neelde[j] stands for postfix
            if i == -1 or needle[i] == needle[j]:
                i, j = i + 1, j + 1
                next[j] = i
            else:
                i = next[i]
            print i,j,next[i],next[j]
        #check through the haystack using next, need O(m) time
        i = j = 0
        while i < m and j < n:
            if j == -1 or haystack[i] == needle[j]:
                i, j = i + 1, j + 1
            else:
                j = next[j]
        if j == n:
            return i - j
        return -1

def evaluate(function, tests):
    for test in tests:
        actual = function(**test['Input'])
        expect = test['Output']
        print('Actual output:', actual)
        print('Expected output:', expect)
        print('Passed?', actual == expect)
        print('\n')

test0 = {'Input':
                 {'haystack': 'hello',
                  'needle': 'll'
                  },
         'Output': 2
         }

test1 = {'Input':
                 {'haystack': 'aaaaa',
                  'needle': 'bba'
                  },
         'Output': -1
         }

test2 = {'Input':
                 {'haystack': 'a',
                  'needle': 'a'
                  },
         'Output': 0
         }

tests = [test0, test1, test2]

def main():
    solution = Solution()
    evaluate(solution.strStr, tests)

if __name__ == '__main__':
    main()
