def evaluate(function, tests):
    for test in tests:
        actual = function(**test['Input'])
        expect = test['Output']
        print(':', actual == expect)

test0 = {'Input':
                 {'nums1': [1,2,2,1],
                  'nums2': [2,2]
                  },
         'Output': [2,2]
         }

test1 = {'Input':
                 {'nums1': [4,9,5],
                  'nums2': [9,4,9,8,4]
                  },
         'Output': [4,9]
         }

test2 = {'Input':
                 {'nums1': [3,6],
                  'nums2': [2,1]
                  },
         'Output': []
         }

tests = [test0, test1, test2]

#%% My solution - hash table
# Time O(m+n) Space O(m+n)
def intersect(nums1, nums2):
    table = {}
    intersection = []
    for n1 in nums1:
        count = table.get(n1, 0)
        table[n1] = count + 1 # table[n1] = table.get(n1, 0) + 1
    for n2 in nums2:
        count = table.get(n2, 0)
        if count > 0:
            intersection.append(n2)
        table[n2] = count - 1
    return intersection

for test in tests:
    print(intersect(**test['Input']))
# evaluate(intersect, tests)

# Follow up:
# What if the given array is already sorted? How would you optimize your algorithm?
# Use two pointers, save space. Time O(M+N) Space O(1)
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# Hash table on nums1 is better. Time O(M+N) Space O(M)
# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
# Map reduce
# If nums1 fits into the memory, we can use Approach 1 which stores all elements of nums1 in the HashMap. Then, we can sequentially load and process nums2.
# If neither nums1 nor nums2 fits into the memory, we split the numeric range into numeric sub-ranges that fit into the memory.
# We modify Approach 1 to count only elements which belong to the given numeric sub-range.
# We process each numeric sub-ranges one by one, util we process all numeric sub-ranges.
# For example:
# Input constraint:
# 1 <= nums1.length, nums2.length <= 10^10.
# 0 <= nums1[i], nums2[i] < 10^5
# Our memory can store up to 1000 elements.
# Then we split numeric range into numeric sub-ranges [0...999], [1000...1999], ..., [99000...99999], then call Approach 1 to process 100 numeric sub-ranges.

# Inspired by the discussion
# Use Pytho Counter function
# Time O(M + N) Space O(min(M, N))
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2): return self.intersect(nums2, nums1)

        cnt = Counter(nums1)
        ans = []
        for x in nums2:
            if cnt[x] > 0:
                ans.append(x)
                cnt[x] -= 1
        return ans

# Sort then Two pointers
# Time O(MlogM + NlogN) Space O(1)
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        ans = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                ans.append(nums1[i])
                i += 1
                j += 1
        return ans
