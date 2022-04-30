# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # My solution - Recursion
    # Time O(depth) Space O(log n)
    def isSymmetric(self, root: TreeNode) -> bool:

        def symmetric(leftNode, rightNode):
            if leftNode is None and rightNode is None:
                return True
            elif leftNode is None or rightNode is None:
                return False
            # Below is another logic
            #if not leftNode or not rightNode:
                #return not leftNode and not rightNode

            return leftNode.val == rightNode.val and \
                   symmetric(leftNode.left, rightNode.right) and \
                   symmetric(leftNode.right, rightNode.left)

        return symmetric(root.left, root.right)

    def isSymmetric1(self, root: TreeNode) -> bool:

        def symmetric(leftNode, rightNode):
            if leftNode and rightNode:
                return leftNode.val == rightNode.val and \
                       symmetric(leftNode.left, rightNode.right) and \
                       symmetric(leftNode.right, rightNode.left)
            return leftNode == rightNode

        return symmetric(root.left, root.right)

    # Iteration - use Stack
    def isSymmetric2(self, root: TreeNode) -> bool:
        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val == right.val:
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
            else:
                return False
        return True


root1 = TreeNode(1)
root1.left = TreeNode(2, TreeNode(3), TreeNode(4))
root1.right = TreeNode(2, TreeNode(4), TreeNode(3))

root2 = TreeNode(1)
root2.left = TreeNode(2, None, TreeNode(3))
root2.right = TreeNode(2, None, TreeNode(3))

root3 = TreeNode(3)

root4 = TreeNode(4)
root4.left = TreeNode(4, TreeNode(4))

def evaluate(function, tests):
    for test in tests:
        actual = function(**test['Input'])
        expect = test['Output']
        print(':', actual == expect)

test0 = {'Input':
                 {'root': root1
                  },
         'Output': True
         }

test1 = {'Input':
                 {'root': root2
                  },
         'Output': False
         }

test2 = {'Input':
                 {'root': root3
                  },
         'Output': True
         }

tests = [test0, test1, test2]

def main():
    solution = Solution()
    evaluate(solution.isSymmetric, tests)
    evaluate(solution.isSymmetric1, tests)
    evaluate(solution.isSymmetric2, tests)

if __name__ == '__main__':
    main()
