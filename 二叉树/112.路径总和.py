# 递归法
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        return self.traversal(root, targetSum - root.val)
        
    def traversal(self, node, num):
        if not node.left and not node.right: # 遇到叶子节点时
            return num == 0 # 为0则返回True，不为0则返回False
        if node.left: # 左
            num -= node.left.val
            if self.traversal(node.left, num): # 如果找到路径，向上传递
                return True
            num += node.left.val # 回溯
        if node.right: # 右
            num -= node.right.val
            if self.traversal(node.right, num): # 如果找到路径，向上传递
                return True
            num += node.right.val # 回溯
            
        return False

# 递归精简版
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right and targetSum == root.val:
            return True
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

# 迭代法：栈内存pair<节点指针，路径总和>
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        # 栈里要放的是pair<节点指针，路径总和>
        stack = [(root, root.val)]
        while stack:
            node, path_sum = stack.pop()
            # 如果该节点是叶子节点，同时该节点的路径总和等于sum，返回True
            if not node.left and not node.right and path_sum == targetSum:
                return True
            # 右节点，压入栈并记录路径总和
            if node.right:
                stack.append((node.right, path_sum + node.right.val))
            # 左节点，压入栈并记录路径总和
            if node.left:
                stack.append((node.left, path_sum + node.left.val))
        return False
