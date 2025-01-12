class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.getDepth(root)
        
    def getDepth(self, root):
        if not root:
            return 0
        left_depth = self.getDepth(root.left) # 左
        right_depth = self.getDepth(root.right) # 右
        height = 1 + max(left_depth, right_depth) # 中
        return height
