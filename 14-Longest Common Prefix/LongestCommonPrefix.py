'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
'''

class Solution:
    # My solution - Divide and Conquer
    def longestCommonPrefix(self, strs: list) -> str:
        return commonPrefix(strs, 0, len(strs)-1)

def commonPrefix(strs, start, end):
    if start == end:
        return strs[start]
    mid = (start + end) // 2
    leftCommon = commonPrefix(strs, start, mid)
    rightCommon = commonPrefix(strs, mid+1, end)
    return compare(leftCommon, rightCommon)

def compare(str1, str2):
    i = 0
    max_l = min(len(str1), len(str2))
    while i < max_l:
        if str1[i] != str2[i]:
            break
        i += 1
    return str1[:i]

# Trie
# https://leetcode.com/problems/longest-common-prefix/solution/
# S is the sum of all characters in all strings
# 1. Horizontal scanning - Time O(S) Space O(1)
# 2. Vertical scanning - Time O(S) Space O(1)
# 3. Divide and Conquer - Time O(S) Space O(m * log n)
# 4. Binary search - Time O(S * log m) Space O(1)


def evaluate(function, tests):
    for test in tests:
        actual = function(**test['Input'])
        expect = test['Output']
        print('Actual output:', actual)
        print('Expected output:', expect)
        print('Passed?', actual == expect)
        print('\n')

test0 = {'Input':
                 {'strs': ["flower","flow","flight"]
                  },
         'Output': 'fl'
         }

test1 = {'Input':
                 {'strs': ["dog","racecar","car"]
                  },
         'Output': ''
         }

test2 = {'Input':
                 {'strs': ['dog']
                  },
         'Output': 'dog'
         }

tests = [test0, test1, test2]

def main():
    solution = Solution()
    evaluate(solution.longestCommonPrefix, tests)

if __name__ == '__main__':
    main()
