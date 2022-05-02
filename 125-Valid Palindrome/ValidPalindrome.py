class Solution:
    # My solution - Two pointers
    # Time O(n) Space O(1)
    def isPalindrome(self, s: str) -> bool:
        #s = s.lower()
        l, r = 0, len(s)-1
        while l < r:
            if s[l].isalnum() and s[r].isalnum():
                if s[l].lower() == s[r].lower():
                    l += 1
                    r -= 1
                else:
                    return False
            elif not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
        return True

#    	i, j = 0, len(s) - 1
#    	while i < j:
#    		a, b = s[i].lower(), s[j].lower()
#    		if a.isalnum() and b.isalnum():
#    			if a != b: return False
#    			else:
#    				i, j = i + 1, j - 1
#    				continue
#    		i, j = i + (not a.isalnum()), j - (not b.isalnum())
#    	return True

#        l, r = 0, len(s)-1
#        while l < r:
#            while l < r and not s[l].isalnum():
#                l += 1
#            while l <r and not s[r].isalnum():
#                r -= 1
#            if s[l].lower() != s[r].lower():
#                return False
#            l +=1; r -= 1
#        return True

    # Pythonic way - list comprehension + if condition
    def isPalindrome2(self, s: str) -> bool:
        s = ''.join(e for e in s if e.isalnum()).lower()
        return s==s[::-1]

    def isPalindrome3(self, s: str) -> bool:
        alphaNum = ''.join(ch.lower() for ch in s if ch.isalnum())
        return alphaNum == ''.join(reversed(alphaNum))

def evaluate(function, tests):
    for test in tests:
        actual = function(**test['Input'])
        expect = test['Output']
        print('Actual:', actual)
        print(':', actual == expect)

test0 = {'Input':
                 {'s': "A man, a plan, a canal: Panama"
                  },
         'Output': True
         }

test1 = {'Input':
                 {'s': "race a car"
                  },
         'Output': False
         }

test2 = {'Input':
                 {'s': " "
                  },
         'Output': True
         }

tests = [test0, test1, test2]

def main():
    solution = Solution()
    evaluate(solution.isPalindrome, tests)

if __name__ == '__main__':
    main()
