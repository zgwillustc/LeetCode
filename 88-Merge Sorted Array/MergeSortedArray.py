def evaluate(function, tests):
    for test in tests:
        actual = function(**test['Input'])
        expect = test['Output']
        print(':', actual == expect)

test0 = {'Input': 
                 {'nums1': [1,2,3,0,0,0],
                  'm': 3,
                  'nums2': [2,5,6],
                  'n': 3
                  },
         'Output': [1,2,2,3,5,6]
         }

test1 = {'Input': 
                 {'nums1': [1],
                  'm': 1,
                  'nums2': [],
                  'n': 0
                  },
         'Output': [1]
         }

test2 = {'Input': 
                 {'nums1': [0],
                  'm': 0,
                  'nums2': [1],
                  'n': 1
                  },
         'Output': [1]
         }

tests = [test0, test1, test2]

#%% My solution
# Time O(m+n) Space O(1)
def merge(nums1, m: int, nums2, n: int) -> None:
    i, j = m-1, n-1
    while i >= 0 and j >= 0:
        # print('i: ', i, 'j:', j)
        if nums1[i] > nums2[j]:
            nums1[i+j+1] = nums1[i]
            i -= 1
        else:
            nums1[i+j+1] = nums2[j]
            j -= 1
    if i < 0:
        nums1[:j+1] = nums2[:j+1]

#%% Inspired by Discussion
def merge2(nums1, m: int, nums2, n: int) -> None:
    while n:
        if m and nums1[m - 1] >= nums2[n - 1]:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1
        else:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1

#%% use Python list method sort()
def merge3(nums1, m: int, nums2, n: int) -> None:
    nums1[m:] = nums2
    nums1.sort()

#%%
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

merge(nums1, m, nums2, n)
print(nums1 == [1,2,2,3,5,6], nums1)
#%%
nums1 = [1]
m = 1
nums2 = []
n = 0

merge(nums1, m, nums2, n)
print(nums1 == [1], nums1)
#%%
nums1 = [0]
m = 0
nums2 = [1]
n = 1

merge(nums1, m, nums2, n)
print(nums1 == [1], nums1)
#%%
nums1 = [2,0]
m = 1
nums2 = [1]
n = 1

merge(nums1, m, nums2, n)
print(nums1 == [1,2], nums1)
#%%
nums1 = [2,3,0]
m = 2
nums2 = [1]
n = 1

merge(nums1, m, nums2, n)
print(nums1 == [1,2,3], nums1)