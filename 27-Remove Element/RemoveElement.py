'''
Given an integer array nums and an integer val, remove all occurrences of val
in nums in-place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages,
you must instead have the result be placed in the first part of the array nums.
More formally, if there are k elements after removing the duplicates,
then the first k elements of nums should hold the final result.
It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying
the input array in-place with O(1) extra memory.

Custom Judge:
The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}

If all assertions pass, then your solution will be accepted.

Example 1:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).

Constraints:
0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100
'''
class Solution:
    # My solution - Seems slow
    # Time O(n) Space O(1)
    def removeElement2(self, nums: list, val: int) -> int:
        pointer = None
        k = len(nums)
        for i in range(len(nums)):
            if nums[i] == val:
                if pointer == None:
                    pointer = i
                nums[i] = None
                k -= 1
            elif pointer != None:
                nums[pointer], nums[i] = nums[i], nums[pointer]
                pointer += 1
            #print(nums)
        return k

    # Inspired by the Hints - two pointers and do not care the order of the resulting nums
    # In average case, it is faster than single pointer
    # Time O(n) Space O(1)
    def removeElement3(self, nums: list, val: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1
        return left

    # Inspired by the solution - two pointers - fast and slow pointers.
    # Time O(n) Space O(1)
    def removeElement4(self, nums: list, val: int) -> int:
        i = 0 # slow pointer, also denotes the number of distinct values
        for j in range(len(nums)): # faster pointer, find the next distint value position
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i

    # Time O(n) Space O(1)
    def removeElement5(self, nums: list, val: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            if nums[left] == val:
                nums[left] = nums[right-1] # reduce array size by 1
                right -= 1
            else:
                left += 1
        return right

    # use python list remove() method
    def removeElement(self, nums: list, val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)

def evaluate(function, tests):
    for test in tests:
        actual = function(**test['Input'])
        expect = test['Output']
        print('Actual output:', actual)
        print('Expected output:', expect)
        print('Passed?', actual == expect)
        print('\n')

test0 = {'Input':
                 {'nums': [3,2,2,3],
                  'val': 3
                  },
         'Output': 2
         }

test1 = {'Input':
                 {'nums': [0,1,2,2,3,0,4,2],
                  'val': 2
                  },
         'Output': 5
         }

test2 = {'Input':
                 {'nums': [2,2,4,4],
                  'val': 5
                  },
         'Output': 4
         }

test3 = {'Input':
                 {'nums': [],
                  'val': 5
                  },
         'Output': 0
         }

tests = [test0, test1, test2, test3]

def main():
    solution = Solution()
    evaluate(solution.removeElement, tests)

if __name__ == '__main__':
    main()
