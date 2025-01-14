# 递归法
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.leftSum(root)
    
    def leftSum(self, node):
        if not node:
            return 0
        # 遇到叶子结点时
        if not node.left and not node.right: # 其实这个也可以不写，如果不写不影响结果，但就会让递归多进行了一层
            return 0
        left_num = self.leftSum(node.left) # 左
        if node.left and not node.left.left and not node.left.right: # 左子树是左叶子节点
            left_num = node.left.val

        right_num = self.leftSum(node.right) # 右

        sum = left_num + right_num # 中
        return sum

# 递归精简版
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_sum = 0
        if root.left and not root.left.left and not root.left.right: # 左子树为左叶子节点
            left_sum = root.left.val
        return left_sum + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

# 迭代法：前序遍历
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [root]
        result = 0
        while stack:
            node = stack.pop()
            if node.left and not node.left.left and not node.left.right: # 左子树为左叶子节点
                result += node.left.val
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return result
