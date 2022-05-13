'''
Given a sorted array of distinct integers and a target value, return the index
if the target is found. If not, return the index where it would be if it were
inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Constraints:
1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums contains distinct values sorted in ascending order.
-10^4 <= target <= 10^4
'''
from typing import List
class Solution:
    # My solution - binary search
    def searchInsert2(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        left = min(left, len(nums)-1)
        right = max(0, right)
        if nums[right] > target:
            return right
        elif nums[left] < target:
            return left+1
        else:
            return left

## https://leetcode.com/problems/search-insert-position/discuss/423166/Binary-Search-101

    def searchInsert3(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)
        while low < high:
            mid = (low + high) // 2
            if target > nums[mid]:
                low = mid + 1
            else:
                high = mid
        return low

    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return left

        # if nums has duplicates
        #l , r = 0, len(nums)-1
        #while l <= r:
        #    mid=(l+r)/2
        #    if nums[mid] < target:
        #        l = mid+1
        #    else:
        #        if nums[mid]== target and nums[mid-1]!=target:
        #            return mid
        #        else:
        #            r = mid-1
        #return l

def evaluate(function, tests):
    for test in tests:
        actual = function(**test['Input'])
        expect = test['Output']
        print('Actual output:', actual)
        print('Expected output:', expect)
        print('Passed?', actual == expect)
        print('\n')

test0 = {'Input':
                 {'nums': [1,3,5,6],
                  'target': 5
                  },
         'Output': 2
         }

test1 = {'Input':
                 {'nums': [1,3,5,6],
                  'target': 2
                  },
         'Output': 1
         }

test2 = {'Input':
                 {'nums': [1,3,5,6],
                  'target': 7
                  },
         'Output': 4
         }

test3 = {'Input':
                 {'nums': [1],
                  'target': 0
                  },
         'Output': 0
         }

test4 = {'Input':
                 {'nums': [1,3],
                  'target': 0
                  },
         'Output': 0
         }

tests = [test0, test1, test2, test3]

def main():
    solution = Solution()
    evaluate(solution.searchInsert, tests)

if __name__ == '__main__':
    main()
