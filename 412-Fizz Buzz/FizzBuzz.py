class Solution:
    # My solution
    def fizzBuzz(self, n: int):
        result = [str(i+1) for i in range(n)]
        helper(3, 'Fizz', n, result)
        helper(5, 'Buzz', n, result)
        helper(15, 'FizzBuzz', n, result)
        return result

def helper(divider, string, n, result):
    idx = divider
    while idx <= n:
        result[idx-1] = string
        idx += divider

    # Inspired by the Discussion
    def fizzBuzz2(self, n):
        return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]

    # Inspired by the Discussion
    def fizzBuzz3(self, n: int):
    	res = []

    	for i in range(1, n + 1):
    		if not i % 3 and not i % 5:
    			res.append("FizzBuzz")

    		elif not i % 3:
    			res.append("Fizz")

    		elif not i % 5:
    			res.append("Buzz")

    		else:
    			res.append(str(i))

    	return res

def evaluate(function, tests):
    for test in tests:
        actual = function(**test['Input'])
        expect = test['Output']
        print('Actual output:', actual)
        print('Expected output:', expect)
        print('Passed?', actual == expect)
        print('\n')

test0 = {'Input':
                 {'n': 3
                  },
         'Output': ["1","2","Fizz"]
         }

test1 = {'Input':
                 {'n': 5
                  },
         'Output': ["1","2","Fizz","4","Buzz"]
         }

test2 = {'Input':
                 {'n': 15
                  },
         'Output': ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
         }

tests = [test0, test1, test2]

def main():
    solution = Solution()
    evaluate(solution.fizzBuzz, tests)

if __name__ == '__main__':
    main()
