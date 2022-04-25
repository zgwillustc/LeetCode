class Solution:
    # My 1st solution
    # Time O(m+n) Space O(m) but seems very slow
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        memo = list(s)
        for char in t:
            try:
                memo.remove(char)
            except:
                return False
        return True

    # My 2nd solution
    # Similar to 1st solution
    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        memo = {}
        for char in s:
            memo[char] = memo.get(char, 0) + 1
        for char in t:
            try:
                memo[char] -= 1
                if memo[char] == 0:
                    memo.pop(char)
            except:
                return False
        return True

    # My 3rd solution - sort first
    # Time O(mlogm + nlogn) Space O(m+n)
    def isAnagram3(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

def evaluate(function, tests):
    for test in tests:
        actual = function(**test['Input'])
        expect = test['Output']
        print(':', actual == expect)

test0 = {'Input':
                 {'s': "anagram",
                  't': "nagaram"
                  },
         'Output': True
         }
test1 = {'Input':
                 {'s': 'rat',
                  't': 'car'
                  },
         'Output': False
         }
test2 = {'Input':
                 {'s': 'care',
                  't': 'race'
                  },
         'Output': True
         }
tests = [test0, test1, test2]

def main():
    solution = Solution()
    evaluate(solution.isAnagram3, tests)

if __name__ == '__main__':
    main()
