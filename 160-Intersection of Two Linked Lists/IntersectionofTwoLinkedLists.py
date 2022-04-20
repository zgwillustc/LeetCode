class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
N0, N1, N2, N3, N4 = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
N0.next, N1.next, N2.next, N3.next = N1, N2, N3, N4

M0, M1 = ListNode(1), ListNode(2)
M0.next = M1

S0 = None

#%%
def evaluate(function, tests):
    for test in tests:
        actual = function(**test['Input'])
        expect = test['Output']
        print('Pass?', actual == expect)

test0 = {'Input': 
                 {'head': N0,
                  },
         'Output': N4
         }

test1 = {'Input': 
                 {'head': M0,
                  },
         'Output': M1
         }

test2 = {'Input': 
                 {'head': S0,
                  },
         'Output': None
         }

tests = [test0, test1, test2]

#%%
# Memorization
# Time O(m+n) Space O(m)
def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    memo = {}
    while headA:
        memo[headA] = headA.val
        headA = headA.next
    while headB:
        if headB in memo: 
            return headB
        else:
            headB = headB.next
    return None

#%%
# Inspired by Discussion
# Time O(m+n) Space O(1)
# Like compare listA+listB and listB+listA
def getIntersectionNode2(headA: ListNode, headB: ListNode) -> ListNode:
    a, b = headA, headB
    while (a != b):
        a = headB if not a else a.next
        b = headA if not b else b.next
    return a    


