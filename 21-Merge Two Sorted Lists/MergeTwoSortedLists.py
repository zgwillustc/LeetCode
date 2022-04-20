def evaluate(function, tests):
    for test in tests:
        actual = function(**test['Input'])
        expect = test['Output']
        print(':', actual == expect)

test0 = {'Input': 
                 {'list1': [1,2,4],
                  'list2': [1,3,4]
                  },
         'Output': [1,1,2,3,4,4]
         }

test1 = {'Input': 
                 {'List1': [],
                  'List2': []
                  },
         'Output': []
         }

test2 = {'Input': 
                 {'List1': [],
                  'List2': [0]
                  },
         'Output': [0]
         }

tests = [test0, test1, test2]
     
#%%
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Brute force solution - the use of dummy head for linked list
# time complexity O(m+n)
# space complexity O(1)
def mergeTwoLists(list1, list2):
    dummy = temp = ListNode()   # dummy and temp are `pointers` that point to a memory location
                                # later only temp is changed to the new location while dummy always points to the same initial location
    while list1 and list2:      # iterate until one of the remaining lists is empty
        if list1.val < list2.val:
            temp.next = list1   # move pointers
            list1 = list1.next
        else:
            temp.next = list2
            list2 = list2.next
        temp = temp.next
    temp.next = list1 or list2  # Connect to the unempty remaining list. This is a useful way to use `or`
    return dummy.next

# Recursion solution
def mergeTwoLists2(list1, list2):
    if list1 or list2:
        return list2 or list1
    if list1.val < list2.val:
        list1.next = mergeTwoLists2(list1.next, list2)
        return list1
    else:
        list2.next = mergeTwoLists2(list1, list2.next)
        return list2
        




