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
# Iteration
# Time O(n) Space O(1)
def reverseList(head):
    if not head:
        return
    L, M, R = None, head, head.next
    while M and R:
        # print(M.val, R.val)
        M.next, L, M, R = L, M, R, R.next
    M.next = L
    return M

    # Inspired by the Discussion
    # prev = None
    # while head:
    #     curr = head
    #     head = head.next
    #     curr.next = prev
    #     prev = curr
    # return prev
    
    # cur, prev = head, None
    # while cur:
    #     cur.next, prev, cur = prev, cur, cur.next
    # return prev

# Recursion 
# Inspired by the Discussion
# Time O(n) Space O(n)
def reverseList2(head):
    if not head or not head.next:
        return head
    node = reverseList2(head.next)
    head.next.next = head # reverse the link
    head.next = None
    return node


