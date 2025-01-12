# 前序遍历
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

# 后序遍历
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        
        return root

# 层序遍历
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        queue = collections.deque([root])
        while queue:
            cur = queue.popleft()
            cur.left, cur.right = cur.right, cur.left
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        
        return root
