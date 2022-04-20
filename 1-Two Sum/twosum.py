nums = [2,7,11,15]
target = 9

output = [0,1]


nums = [3,2,4]
target = 6

output = [1,2]

nums = [3,3]
target = 6

output = [0,1]

# Brute force - O(n*n)
def twoSum(nums, target):
    n = len(nums)
    # if n < 2:
    #     return None, None
    for i in range(n-1):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return i, j
    return None, None
    
# Memorization - O(n)
def twoSum(nums, target):
    seen = {}    
    for idx, value in enumerate(nums):        
        remain = target - value
        if remain in seen:
            return idx, seen[remain]
        else:
            seen[value] = idx
    


