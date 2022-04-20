output0 = [1,3,12,0,0]
output1 = [0]
output2 = [1,6,0]

#%% My solution - Two pointers
# Time O(n) Space(1)
def moveZeroes(nums) -> None:
    left, right = 0, len(nums)-1
    while left < right:
        if nums[left] == 0:
            nums[right], nums[left:right] = nums[left], nums[left+1:right+1]
            right -= 1
        else:
            left +=1

nums0 = [0,1,0,3,12]
nums1 = [0]
nums2 = [1,6,0]
moveZeroes(nums0)
moveZeroes(nums1)
moveZeroes(nums2)
print(output0 == nums0)
print(output1 == nums1)
print(output2 == nums2)

#%% Better Two pointers
# Time O(n) Space(1)
def moveZeroes(nums) -> None:
    lastNonZero = 0
    for cur in range(len(nums)):
        if nums[cur] != 0:
            nums[lastNonZero], nums[cur] = nums[cur], nums[lastNonZero]
            lastNonZero += 1

nums0 = [0,1,0,3,12]
nums1 = [0]
nums2 = [1,6,0]
moveZeroes(nums0)
moveZeroes(nums1)
moveZeroes(nums2)
print(output0 == nums0)
print(output1 == nums1)
print(output2 == nums2)

#
class Solution:
    def moveZeroes(self, nums: list) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            # wait while we find a non-zero element to
            # swap with you
            if nums[slow] != 0:
                slow += 1
