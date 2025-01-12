# 递归法1
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.getDepth(root)
    
    def getDepth(self, root):
        if not root:
            return 0
        left_depth = self.getDepth(root.left) # 左
        right_depth = self.getDepth(root.right) # 右
        # 当左子树为空，右子树不为空时，说明这不是最低叶子结点
        if not root.left and root.right:
            return 1 + right_depth
        
        # 当右子树为空，左子树不为空时，说明这不是最低叶子结点
        if not root.right and root.left:
            return 1 + left_depth
        
        result = 1 + min(left_depth, right_depth)
        return result


# 递归法2
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and root.right:
            return 1 + self.minDepth(root.right)
        if root.left and not root.right:
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
