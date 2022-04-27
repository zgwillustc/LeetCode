# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # My previous recursive solution
    # list concatenate is not a fast method
    # def inorderTraversal(self, root: TreeNode) -> list:
    #     if root is None:
    #         return []
    #     return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

    # My soution - recursion
    # Time O(n) Space O(n)
    def inorderTraversal(self, root: TreeNode) -> list:
        result = []
        def recursion(node, result):
            if node == None:
                return
            recursion(node.left, result)
            result.append(node.val)
            recursion(node.right, result)
        recursion(root, result)
        return result
    
    # Iteration using Stack - inspired by the Solution
    # Time O(n) Space O(n)
    def inorderTraversal2(self, root: TreeNode) -> list:
        result, stack = [], []
        current = root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)
            current = current.right
        return result
    
    # Another iterative method - inspired by Discussion
    def inorderTraversal3(self, root: TreeNode) -> list:
        res, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()  # the last element
            if node:
                if visited:
                    res.append(node.val)
                else:  # inorder: left -> root -> right
                    stack.append((node.right, False))
                    stack.append((node, True))
                    stack.append((node.left, False))
        return res
    
    # Morris Traversal - inspired by the Solution
    # Time O(n) Space O(1)
    def inorderTraversal4(self, root: TreeNode) -> list:
        res = []
        pre = curr = root
        while curr:
            if curr.left:
                pre = curr.left
                while pre.right:
                    pre = pre.right
                pre.right = curr
                temp = curr
                curr = curr.left
                temp.left = None
            else:
                res.append(curr.val)
                curr = curr.right
        return res

root1 = TreeNode(1)
root1.right = TreeNode(2, TreeNode(3))

root2 = None

root3 = TreeNode(1)


def evaluate(function, tests):
    for test in tests:
        actual = function(**test['Input'])
        expect = test['Output']
        print(':', actual == expect)

test0 = {'Input':
                 {'root': root1
                  },
         'Output': [1,3,2]
         }

test1 = {'Input':
                 {'root': root2
                  },
         'Output': []
         }

test2 = {'Input':
                 {'root': root3
                  },
         'Output': [1]
         }

tests = [test0, test1, test2]

def main():
    solution = Solution()
    # evaluate(solution.inorderTraversal, tests)
    # evaluate(solution.inorderTraversal2, tests)
    evaluate(solution.inorderTraversal4, tests)

if __name__ == '__main__':
    main()
