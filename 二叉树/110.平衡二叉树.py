# 递归：后序遍历
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.getHeight(root) != -1:
            return True
        else:
            return False

    def getHeight(self, root):
        # 1.终止条件
        if not root:
            return 0
        # 左
        """
        :=（赋值表达式）
        left_height := self.get_height(root.left) 的含义是：
        调用函数 self.get_height(root.left) 的返回值赋值给变量 left_height。
        同时将这个值用于条件判断。
        """
        if (left_height := self.getHeight(root.left)) == -1:
            return -1            
        # 右
        if (right_height := self.getHeight(root.right)) == -1:
            return -1
        # 中
        if abs(left_height - right_height) > 1:
            return -1
        else:
            return 1 + max(left_height, right_height)

# 精简版
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.getHeight(root) != -1

    def getHeight(self, node):
        if not node:
            return 0
        left = self.getHeight(node.left)
        right = self.getHeight(node.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1
