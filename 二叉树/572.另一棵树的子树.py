class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot: # 两棵树都为空
            return True
        if not root: # root为空，但 subRoot 不为空
            return False
        
        # 检查当前树是否与 subRoot 相同，或递归检查左右子树
        return self.isSub(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSub(self, root, sub_root):
        if not root and not sub_root:
            return True
        elif not root and sub_root:
            return False
        elif root and not sub_root:
            return False
        elif root.val != sub_root.val:
            return False
        
        # 此时两个节点不为空且数值相同，开始递归
        left = self.isSub(root.left, sub_root.left) # 左
        right = self.isSub(root.right, sub_root.right) # 右
        is_same = left and right # 中
        return is_same
