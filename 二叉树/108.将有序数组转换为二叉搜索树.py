# 递归法
class Solution:
    def traversal(self, nums: List[int], left: int, right: int) -> TreeNode:
        if left > right:
            return None
        
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        root.left = self.traversal(nums, left, mid-1)
        root.right = self.traversal(nums, mid+1, right)

        return root

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.traversal(nums, 0, len(nums)-1)

# 递归精简版
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[: mid])
        root.right = self.sortedArrayToBST(nums[mid+1 :])
        return root
