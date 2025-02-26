# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    1. 确定递归函数参数和返回值: 返回的一个长度为2的数组，表示当前节点偷 dp[1] 与不偷 dp[0] 的两个状态下获得的最大金钱数量
    2. 确定终止条件: 遇到空节点则返回[0, 0]
    3. 确定遍历顺序: 后序遍历
    4. 确定单层递归逻辑: 偷当前节点...; 不偷当前节点...
    5. 举例推导dp数组:
    """
    def rob(self, root: Optional[TreeNode]) -> int:
        dp = self.traversal(root)
        return max(dp)
    
    def traversal(self, node):
        # 递归终止条件，遇到空节点
        if not node:
            return (0, 0)
        
        left = self.traversal(node.left)
        right = self.traversal(node.right)

        # 不偷当前节点
        val_0 = max(left[0], left[1]) + max(right[0], right[1])
        
        # 偷当前节点
        val_1 = node.val + left[0] + right[0]

        return (val_0, val_1)
