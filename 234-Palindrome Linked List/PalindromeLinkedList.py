class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
N0, N1, N2, N3 = ListNode(1), ListNode(2), ListNode(2), ListNode(1)
N0.next, N1.next, N2.next = N1, N2, N3

M0, M1 = ListNode(1), ListNode(2)
M0.next = M1

S0 = ListNode(3)

#%%
def evaluate(function, tests):
    for test in tests:
        actual = function(**test['Input'])
        expect = test['Output']
        print('Pass?', actual == expect)

test0 = {'Input': 
                 {'head': N0,
                  },
         'Output': True
         }

test1 = {'Input': 
                 {'head': M0,
                  },
         'Output': False
         }

test2 = {'Input': 
                 {'head': S0,
                  },
         'Output': True
         }

tests = [test0, test1, test2]

#%%
# Memorization
# Time O(n)
# Space O(n)
def isPalindrome(head: ListNode) -> bool:
    # This is redundunt
    # memo = []
    # point = head
    # while point:
    #     memo.append(point.val)
    #     point = point.next
    # L = len(memo)
    # if L % 2: # odd length
    #     if memo[:L//2 + 1] == memo[L//2:][::-1]:
    #         return True
    # elif L % 2 == 0:
    #     if memo[:L//2] == memo[L//2:][::-1]:
    #         return True
    # else: 
    #     return False
    
    # Inspired by the Discussion
    memo = []
    point = head
    while point:
        memo.append(point.val)
        point = point.next
    return memo == memo[::-1]

evaluate(isPalindrome, tests)        
    
#%% 
# Two pointers - fast and slow pointers
def isPalindrome2(head: ListNode) -> bool:
    if not head or not head.next:
        return True

    slow = fast = head
    reversed_list = None

    # reverse left half of the list while searching
    # the start point of the right half
    while fast is not None and fast.next is not None:
        tmp = slow

        # keep moving guys
        slow = slow.next
        fast = fast.next.next

        # place node at the start of the reversed half
        tmp.next = reversed_list
        reversed_list = tmp

    # if there are even number of elements in the list
    # do one more step to reach the first element of
    # the second list's half
    if fast is not None:
        slow = slow.next

    # compare reversed left half with the original
    # right half
    while reversed_list is not None and reversed_list.val == slow.val:
        reversed_list = reversed_list.next
        slow = slow.next

    return reversed_list is None

# Or
def isPalindrome3(head: ListNode) -> bool:
    fast = slow = head
    # find the mid node
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    # reverse the second half
    node = None
    while slow:
        nxt = slow.next
        slow.next = node
        node = slow
        slow = nxt
    # compare the first and second half nodes
    while node: # while node and head:
        if node.val != head.val:
            return False
        node = node.next
        head = head.next
    return True

#%% Others
def isPalindrome(head):
    rev = None
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next
    while rev and rev.val == slow.val:
        slow = slow.next
        rev = rev.next
    return not rev

def isPalindrome(head):
    rev = None
    fast = head
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, head = head, rev, head.next
    tail = head.next if fast else head
    isPali = True
    while rev:
        isPali = isPali and rev.val == tail.val
        head, head.next, rev = rev, head, rev.next
        tail = tail.next
    return isPali


