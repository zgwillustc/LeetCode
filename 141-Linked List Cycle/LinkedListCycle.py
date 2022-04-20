def evaluate(function, tests):
    for test in tests:
        actual = function(**test['Input'])
        expect = test['Output']
        print(':', actual == expect)

test0 = {'Input': 
                 {'s': ["h","e","l","l","o"],
                  },
         'Output': ["o","l","l","e","h"]
         }

test1 = {'Input': 
                 {'s': ["H","a","n","n","a","h"],
                  },
         'Output': ["h","a","n","n","a","H"]
         }

test2 = {'Input': 
                 {'s': ['m'],
                  },
         'Output': ['m']
         }

tests = [test0, test1, test2]

#%%
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
N0, N1, N2, N3 = ListNode(3), ListNode(2), ListNode(0), ListNode(-4)
N0.next, N1.next, N2.next, N3.next = N1, N2, N3, N1

M0, M1 = ListNode(1), ListNode(2)
M0.next, M1.next = M1, M0

S0 = ListNode(1)
S0.next = S0

#%%
# Memorization
# Time complexity: O(n)
# Space complexity: O(n)
def hasCycle(head):
#    if not head: # This is not necessary
#        return False
    memo = []
    curr = head
    while curr.next:
        if curr in memo:
            return True
        else:
            memo.append(curr)
            curr = curr.next
    return False

# Two pointers
# Fast and slow pointers
# O(1) space complexity
def hasCycle2(head):
    fast = slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False
    

