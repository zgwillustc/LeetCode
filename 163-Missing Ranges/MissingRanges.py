'''
Given a sorted integer array where the range of elements are in the inclusive
range [lower, upper], return its missing ranges.

For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99,
return [“2”, “4->49”, “51->74”, “76->99”].
'''

class Solution:
    # My solution
    def missingRanges2(self, nums: list, lower: int, upper: int) -> list:
        nums = [lower]+nums+[upper]
        result = []
        for i in range(len(nums)-1):
            if i == 0:
                left = nums[i]-1
            else:
                left = nums[i]
            if i == len(nums)-2:
                right = nums[i+1]+1
            else:
                right = nums[i+1]
            item = rangeToStr(left, right)
            if item:
                result.append(item)
        return result
    # Modified
    def missingRanges(self, nums: list, lower: int, upper: int) -> list:
        nums = [lower-1]+nums+[upper+1]
        result = []
        for i in range(len(nums)-1):
            item = rangeToStr(nums[i], nums[i+1])
            if item:
                result.append(item)
        return result

def rangeToStr(left, right):
    if right - left == 2:
        return f'{left+1}'
    elif right- left > 2:
        return f'{left+1}->{right-1}'

def evaluate(function, tests):
    for test in tests:
        actual = function(**test['Input'])
        expect = test['Output']
        print('Actual output:', actual)
        print('Expected output:', expect)
        print('Passed?', actual == expect)
        print('\n')

test0 = {'Input':
                 {'nums': [0, 1, 3, 50, 75],
                  'lower': 0,
                  'upper': 99
                  },
         'Output': ["2", "4->49", "51->74", "76->99"]
         }

test1 = {'Input':
                 {'nums': [0, 1, 2, 3, 7],
                  'lower': 0,
                  'upper': 7
                  },
         'Output': ["4->6"]
         }

test2 = {'Input':
                 {'nums': [1, 2, 3, 4],
                  'lower': 1,
                  'upper': 4
                  },
         'Output': []
         }

test3 = {'Input':
                 {'nums': [],
                  'lower': 1,
                  'upper': 4
                  },
         'Output': ['1->4']
         }

tests = [test0, test1, test2, test3]

def main():
    solution = Solution()
    evaluate(solution.missingRanges, tests)

if __name__ == '__main__':
    main()
