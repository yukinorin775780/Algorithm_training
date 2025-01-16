# 递归-前序-修改root1
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # 终止条件：但凡有一个节点为空，就立刻返回另一个。如果另一个也为空，则返回的是None
        if not root1:
            return root2
        if not root2:
            return root1
        
        root1.val += root2.val # 中
        root1.left = self.mergeTrees(root1.left, root2.left) # 左
        root1.right = self.mergeTrees(root1.right, root2.right) # 右

        return root1

# 递归-前序-新建root
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        root = TreeNode()
        root.val = root1.val + root2.val
        root.left = self.mergeTrees(root1.left, root2.left)
        root.right = self.mergeTrees(root1.right, root2.right)

        return root

# 迭代
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        
        queue = collections.deque()
        queue.append(root1)
        queue.append(root2)
        while queue:
            node1 = queue.popleft()
            node2 = queue.popleft()
            # 更新 queue
            # 只有两个节点都有左节点时，再往queue放
            if node1.left and node2.left:
                queue.append(node1.left)
                queue.append(node2.left)
            # 只有两个节点都有右节点时，再往queue放
            if node1.right and node2.right:
                queue.append(node1.right)
                queue.append(node2.right)
            
            # 更新当前节点，同时改变当前节点的左右孩子
            node1.val += node2.val
            if not node1.left and node2.left:
                node1.left = node2.left
            if not node1.right and node2.right:
                node1.right = node2.right
        
        return root1

# 迭代优化版
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        
        queue = deque()
        queue.append((root1, root2))

        while queue:
            node1, node2 = queue.popleft()
            node1.val += node2.val

            if node1.left and node2.left:
                queue.append((node1.left, node2.left))
            elif not node1.left:
                node1.left = node2.left

            if node1.right and node2.right:
                queue.append((node1.right, node2.right))
            elif not node1.right:
                node1.right = node2.right
        
        return root1
