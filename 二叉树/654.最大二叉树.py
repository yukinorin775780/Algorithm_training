class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # 终止条件：子树保证有一个元素即是叶子结点
        if len(nums) == 1:
            return TreeNode(nums[0])

        max_num = float('-inf')
        max_idx = 0
        # 1. 找到数组中最大值以及对应下标，用来分割数组
        for i in range(len(nums)):
            if nums[i] > max_num:
                max_num = nums[i]
                max_idx = i

        root = TreeNode(max_num)
        # 2. 最大值所在下标左区间构造左子树
        if max_idx > 0: # 保证左区间至少有一个数值 
            left_nums = nums[:max_idx]
            root.left = self.constructMaximumBinaryTree(left_nums)
        # 3. 最大值所在下标右区间构造右子树
        if max_idx < len(nums) - 1: # 保证右区间至少有一个数值
            right_nums = nums[max_idx + 1:]
            root.right = self.constructMaximumBinaryTree(right_nums)

        return root

# 利用下标
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return self.traversal(nums, 0, len(nums))

    def traversal(self, nums: List[int], left: int, right: int) -> TreeNode:
        if left >= right:
            return None
        max_idx = left
        for i in range(left+1, right):
            if nums[i] > nums[max_idx]:
                max_idx = i
        root = TreeNode(nums[max_idx])
        root.left = self.traversal(nums, left, max_idx)
        root.right = self.traversal(nums, max_idx+1, right)
        return root

# 利用切片
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        max_num = max(nums)
        max_idx = nums.index(max_num)
        node = TreeNode(max_num)
        node.left = self.constructMaximumBinaryTree(nums[:max_idx])
        node.right = self.constructMaximumBinaryTree(nums[max_idx+1:])

        return node
