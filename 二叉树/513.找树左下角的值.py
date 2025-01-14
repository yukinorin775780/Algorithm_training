# 递归
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.max_depth = float('-inf')
        self.result = None
        self.traversal(root, 0)
        return self.result

    def traversal(self, node, path):
        # 终止条件: 遇到叶子节点时，更新最大深度
        if not node.left and not node.right:
            if depth > self.max_depth:
                self.max_depth = depth
                self.result = node.val
            return
        
        if node.left:
            depth += 1
            self.traversal(node.left, depth)
            depth -= 1 # 回溯
        if node.right:
            depth += 1
            self.traversal(node.right, depth)
            depth -= 1 # 回溯

# 递归精简版
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.max_depth = float('-inf')
        self.result = None
        self.traversal(root, 0)
        return self.result
    
    def traversal(self, node, depth):
        if not node.left and not node.right:
            if depth > self.max_depth:
                self.max_depth = depth
                self.result = node.val
            return
        
        if node.left:
            self.traversal(node.left, depth + 1)
        if node.right:
            self.traversal(node.right, depth + 1)

# 层序遍历
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return root
        
        queue = collections.deque([root])
        
        while queue:
            for i in range(len(queue)):
                cur = queue.popleft()
                # 只更新每一层的第一个节点，到达最后一层时，就是树的左下角
                if i == 0:
                    result = cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return result
