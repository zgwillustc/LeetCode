import collections

class Solution:
    # My solution - Hash table
    # Time O(n) Space O(1) - because English alphabet contains 26 letters
    def firstUniqChar(self, s: str) -> int:
        seen = {}
        for char in s:
            seen[char] = seen.get(char, 0) + 1
        # one line to build the hash map using Counter() - Inspired by the Solution
        # seen = collections.Counter(s)

        for idx, char in enumerate(s):
            if seen[char] == 1:
                return idx
        return -1



def evaluate(function, tests):
    for test in tests:
        actual = function(**test['Input'])
        expect = test['Output']
        print(':', actual == expect)

test0 = {'Input':
                 {'s': 'leetcode'
                  },
         'Output': 0
         }

test1 = {'Input':
                 {'s': 'loveleetcode'
                  },
         'Output': 2
         }

test2 = {'Input':
                 {'s': 'aabb'
                  },
         'Output': -1
         }

tests = [test0, test1, test2]

def main():
    solution = Solution()
    evaluate(solution.firstUniqChar, tests)

if __name__ == '__main__':
    main()
