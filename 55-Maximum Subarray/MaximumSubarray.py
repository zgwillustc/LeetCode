def evaluate(function, tests):
    for test in tests:
        actual = function(**test['Input'])
        expect = test['Output']
        print(':', actual == expect)

test0 = {'Input':
                 {'nums': [-2,1,-3,4,-1,2,1,-5,4],
                  },
         'Output': 6
         }

test1 = {'Input':
                 {'nums': [1],
                  },
         'Output': 1
         }

test2 = {'Input':
                 {'nums': [5,4,-1,7,8],
                  },
         'Output': 23
         }

test3 = {'Input':
                 {'nums': [-2,1],
                  },
         'Output': 1
         }

tests = [test0, test1, test2, test3]

#%% divide and conquer
def maxSubArray(nums) -> int:
    pass

evaluate(maxSubArray, tests)

#%% dynamic programming
# Exceeds time limit
def maxSubArray2(nums) -> int:
    max_sum = nums[0]
    for left in range(len(nums)):
        cur_sum = nums[left]
        max_sum = max(max_sum, cur_sum)
        for right in range(left+1, len(nums)):
            cur_sum += nums[right]
            if cur_sum > max_sum:
                max_sum = cur_sum
    return max_sum
evaluate(maxSubArray2, tests)

#%% Solutions
# Brute Force - Time O(n*n) Space O(1)
class Solution:
    def maxSubArray(self, nums):
        ans = -inf
        for i in range(len(nums)):
            cur_sum = 0
            for j in range(i, len(nums)):
                cur_sum += nums[j]
                ans = max(ans, cur_sum)
        return ans
# Recursion - Time O(n*n) Space O(n)
class Solution:
    def maxSubArray(self, nums):
        def solve(i, must_pick):
            if i >= len(nums): return 0 if must_pick else -inf
            return max(nums[i] + solve(i+1, True), 0 if must_pick else solve(i+1, False))
        return solve(0, False)
# Dynamic Programming - Memorization - Time O(n) Space O(n)
class Solution:
    def maxSubArray(self, nums):
        @cache
        def solve(i, must_pick):
            if i >= len(nums): return 0 if must_pick else -inf
            return max(nums[i] + solve(i+1, True), 0 if must_pick else solve(i+1, False))
        return solve(0, False)
# Dynamic Programming - Memorization - Time O(n) Space O(n)
class Solution:
    def maxSubArray(self, nums):
        dp = [[0]*len(nums) for i in range(2)]
        dp[0][0], dp[1][0] = nums[0], nums[0]
        for i in range(1, len(nums)):
            dp[1][i] = max(nums[i], nums[i] + dp[1][i-1])
            dp[0][i] = max(dp[0][i-1], dp[1][i])
        return dp[0][-1]
class Solution:
    def maxSubArray(self, nums):
        dp = [*nums]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i-1])
        return max(dp)
# Kadane's Algorithm - Time O(n) Space O(1)
class Solution:
    def maxSubArray(self, nums):
        cur_max, max_till_now = 0, -inf
        for c in nums:
            cur_max = max(c, cur_max + c)
            max_till_now = max(max_till_now, cur_max)
        return max_till_now
# Divide and Conquer - Time O(n log n) Space O(log n)
class Solution:
    def maxSubArray(self, nums):
        def maxSubArray(A, L, R):
            if L > R: return -inf
            mid, left_sum, right_sum, cur_sum = (L + R) // 2, 0, 0, 0
            for i in range(mid-1, L-1, -1):
                left_sum = max(left_sum, cur_sum := cur_sum + A[i])
            cur_sum = 0
            for i in range(mid+1, R+1):
                right_sum = max(right_sum, cur_sum := cur_sum + A[i])
            return max(maxSubArray(A, L, mid-1), maxSubArray(A, mid+1, R), left_sum + A[mid] + right_sum)
        return maxSubArray(nums, 0, len(nums)-1)
# Optimized divide and Conquer - Time O(n) Space O(log n)
class Solution:
    def maxSubArray(self, nums):
        pre, suf = [*nums], [*nums]
        for i in range(1, len(nums)):       pre[i] += max(0, pre[i-1])
        for i in range(len(nums)-2,-1,-1):  suf[i] += max(0, suf[i+1])
        def maxSubArray(A, L, R):
            if L == R: return A[L]
            mid = (L + R) // 2
            return max(maxSubArray(A, L, mid), maxSubArray(A, mid+1, R), pre[mid] + suf[mid+1])
        return maxSubArray(nums, 0, len(nums)-1)
