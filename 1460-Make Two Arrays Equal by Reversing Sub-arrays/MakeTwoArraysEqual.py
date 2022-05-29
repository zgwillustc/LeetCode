'''
You are given two integer arrays of equal length target and arr. In one step,
you can select any non-empty sub-array of arr and reverse it. You are allowed
to make any number of steps.

Return true if you can make arr equal to target or false otherwise.


Constraints:
target.length == arr.length
1 <= target.length <= 1000
1 <= target[i] <= 1000
1 <= arr[i] <= 1000
'''
from typing import List

class Solution:
    # Time O(n log n) Space O(n)
    def canBeEqual1(self, target: List[int], arr: List[int]) -> bool:
        return sorted(target) == sorted(arr)

    def canBeEqual2(self, target: List[int], arr: List[int]) -> bool:
        memo = {}
        for num in target:
            memo[num] = memo.get(num, 0) + 1

        for num in arr:
            if num in memo:
                memo[num] -= 1
            else:
                return False
            if memo[num] < 0:
                return False
        return True

    # Time O(n) Space O(n)
    def canBeEqual3(self, target: List[int], arr: List[int]) -> bool:
        return collections.Counter(target) == collections.Counter(arr)

    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        memo = {}
        for i in range(len(target)):
            memo[target[i]] = memo.get(target[i], 0) + 1
            memo[arr[i]] = memo.get(arr[i], 0) - 1

        for val in memo.values():
            if val != 0:
                return False

        return True

def evaluate(function, tests):
    for test in tests:
        actual = function(**test['Input'])
        expect = test['Output']
        print('Actual output:', actual)
        print('Expected output:', expect)
        print('Passed?', actual == expect)
        print('\n')

test0 = {'Input':
                 {'target': [1,2,3,4],
                  'arr': [2,4,1,3]
                  },
         'Output': True
         }

test1 = {'Input':
                 {'target': [7],
                  'arr': [7]
                  },
         'Output': True
         }

test2 = {'Input':
                 {'target': [3,7,9],
                  'arr': [3,7,7]
                  },
         'Output': False
         }

tests = [test0, test1, test2]

def main():
    solution = Solution()
    evaluate(solution.canBeEqual, tests)

if __name__ == '__main__':
    main()
