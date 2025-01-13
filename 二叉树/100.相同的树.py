class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.compare(p, q)
    
    def compare(self, tree1, tree2):
        if not tree1 and tree2: # p树为空，q树不为空
            return False
        elif tree1 and not tree2: # p树不为空，q树为空
            return False
        elif not tree1 and not tree2: # p树、q树都为空
            return True
        elif tree1.val != tree2.val: # p树、q树都不为空时，数值不相等
            return False
        
        # 此时 p、q 树都不为空且数值相等，此时开始递归，做下一层判断
        left = self.compare(tree1.left, tree2.left) # p树：左/q树：左
        right = self.compare(tree1.right, tree2.right) # p树：右/q树：右
        isSame = left and right # p树：中/q树：中
        
        return isSame
