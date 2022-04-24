class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # My solution - recursion
    # Time O(n log n) Space O(n) - because use of Python list slice - Discussion
    def sortedArrayToBST(self, nums) -> TreeNode:
        def recursion(nums):
            if len(nums) == 0:
                return
            mid = len(nums) // 2
            left = recursion(nums[:mid])
            right = recursion(nums[mid+1:])
            return TreeNode(nums[mid], left, right)
        return recursion(nums)

    # Pass lower and upper bounds instead of slicing
    # Time O(n)  Space O(log n)
    def sortedArrayToBST2(self, nums) -> TreeNode:
        def recursion(left, right):
            if left > right:
                return
            mid = (left + right) // 2
            leftNode = recursion(left, mid - 1)
            rightNode = recursion(mid + 1, right)
            return TreeNode(nums[mid], leftNode, rightNode)
        return recursion(0, len(nums) - 1)

def main():
    nums1 = [-10,-3,0,5,9]
    nums2 = [1,3]
    solution = Solution()
    tree1 = solution.sortedArrayToBST(nums1)
    tree2 = solution.sortedArrayToBST(nums2)

if __name__ == '__main__':
    main()
