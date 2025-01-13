# 后序遍历
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        return self.count(root)

    def count(self, node):
        if not node:
            return 0
        left_num = self.count(node.left) # 左
        right_num = self.count(node.right) # 右
        middle_num = left_num + right_num + 1 # 中
        return middle_num

# 精简版，后序遍历
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.countNodes(root.left) + self.countNodes(root.right) + 1

# 层序遍历
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = collections.deque([root])
        sum = 0

        while queue:
            for _ in range(len(queue)):
                sum += 1
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return sum

# 完全二叉树1
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = root.left
        right = root.right
        left_depth = 0
        right_depth = 0
        while left:
            left = left.left
            left_depth += 1
        while right:
            right = right.right
            right_depth += 1
        if left_depth == right_depth:
            return (2 << left_depth) - 1 # 注意(2<<1) 相当于2^2，所以leftDepth初始为0
        
        return self.countNodes(root.left) + self.countNodes(root.right) + 1

# 完全二叉树2
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        count = 1
        left = root.left
        right = root.right
        while left and right:
            count += 1
            left = left.left
            right = right.right
        if not left and not right: # 如果同时到底说明是满二叉树，通过公式计算
            return 2 ** count - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

# 完全二叉树3
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        count = 0
        left = root.left
        right = root.right
        while left and right:
            count += 1
            left = left.left
            right = right.right
        if not left and not right: # 如果同时到底，则是满二叉树
            return (2 << count) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

 
