def evaluate(function, tests):
    for test in tests:
        actual = function(**test['Input'])
        expect = test['Output']
        print(':', actual == expect)

test0 = {'Input':
                 {'nums': [3,2,3]
                  },
         'Output': 3
         }

test1 = {'Input':
                 {'nums': [2,2,1,1,1,2,2]
                  },
         'Output': 2
         }

test2 = {'Input':
                 {'nums': [5]
                  },
         'Output': 5
         }

tests = [test0, test1, test2]

#%% My solution - Memorization - Hash Table
# Time O(n) Space O(n)
def majorityElement(nums) -> int:
    memo = {}
    n = len(nums)
    for num in nums:
        if num in memo:
            memo[num] += 1
        else:
            memo[num] = 1
        if memo[num] > int(n/2): # or use n//2
            return num

    # A simpler version # Inspired by Discussion
#    m = {}
#    for n in nums:
#        m[n] = m.get(n, 0) + 1 # use Python dictionary get() method
#        if m[n] > len(nums)//2:
#            return n

evaluate(majorityElement, tests)

#%% Inspired by the hint - Sort
# Time O(n log n) Space O(n) - Python list.sort() method complexity: timsort
def majorityElement2(nums) -> int:
    nums.sort()
    return nums[int(len(nums)/2)] # or use len(nums)//2

evaluate(majorityElement2, tests)

#%% Majority vote algorithm - Inspired by Discussion
# Time O(n) Space O(1)
def majorityElement3(nums) -> int:
    # We first assume that our first num is the majority element
    # So the count here is 1 as we have seen it 1 times, if the
    # count in the end is greater than 0 we are sure that this is majority element
    # as if you take count of majority element and subtract sum of all counts of non
    # Majority element, if that count is still positive that it proves that is
    # majority element. We do not need to check count in end over here as we are
    # sure that there exists a majority element.
    candidate, count = nums[0], 0
    for num in nums:
        # If the next number is not same as prev
        # and count becomes 0 make this number as majority element and initialize
        # count to 1 again else just decrease the count
        if num == candidate:
            count += 1
        elif count == 0:
            candidate, count = num, 1
        else:
            count -= 1
    return candidate

#%% Other solutions: Divide and Conquer, Bit Manipulation, Randomization

#%% Official solution
# Brute Force
# Time O(n*n) Space O(1)
class Solution:
    def majorityElement(self, nums):
        majority_count = len(nums)//2
        for num in nums:
            count = sum(1 for elem in nums if elem == num)
            if count > majority_count:
                return num
# HashMap
# Time O(n) Space O(n)
class Solution:
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
# Sorting
# Time O(n log n) Space O(n) or O(1)
class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]
# Randomization
# Time O(oo) Space O(1)
import random
class Solution:
    def majorityElement(self, nums):
        majority_count = len(nums)//2
        while True:
            candidate = random.choice(nums)
            if sum(1 for elem in nums if elem == candidate) > majority_count:
                return candidate
# Divide and Conquer
# Time O(n log n) Space O(n log n)
class Solution:
    def majorityElement(self, nums, lo=0, hi=None):
        def majority_element_rec(lo, hi):
            # base case; the only element in an array of size 1 is the majority
            # element.
            if lo == hi:
                return nums[lo]

            # recurse on left and right halves of this slice.
            mid = (hi-lo)//2 + lo
            left = majority_element_rec(lo, mid)
            right = majority_element_rec(mid+1, hi)

            # if the two halves agree on the majority element, return it.
            if left == right:
                return left

            # otherwise, count each element and return the "winner".
            left_count = sum(1 for i in range(lo, hi+1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi+1) if nums[i] == right)

            return left if left_count > right_count else right

        return majority_element_rec(0, len(nums)-1)
# Boyer-Moore Voting Algorithm
# Time O(n) Space O(1)
class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
