# Inspired by the Discussion
def removeDuplicates(nums) -> int:
    left, right, length = 0, 1, len(nums) # two pointers
    while right < length:
        if nums[left] < nums[right]: # if the right pointer hits a new unique number
            left += 1 
            nums[left], nums[right] = nums[right], nums[left] # swap the values of left and right pointers
        right +=1 # the right pointer just travels from start to end
    return left + 1

#%% Also two pointers
def removeDuplicates2(nums) -> int:
    k = 1
    for i in range(len(nums)-1):
        if nums[i] < nums[i+1]:
            nums[k] = nums[i+1]
            k += 1
    return k
    

#%%
nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))


nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates2(nums))

