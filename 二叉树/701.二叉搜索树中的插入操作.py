# 递归法1
class Solution:
    def __init__(self):
        self.pre = None
    
    def traversal(self, cur, val):
        if not cur:
            node = TreeNode(val)
            if val > self.pre.val:
                self.pre.right = node
            else:
                self.pre.left = node
            return
        
        self.pre = cur
        if cur.val > val:
            self.traversal(cur.left, val)
        
        if cur.val < val:
            self.traversal(cur.right, val)

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.pre = TreeNode(0)
        if not root:
            return TreeNode(val)
        self.traversal(root, val)
        return root

# 递归法2
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root or root.val == val:
            return TreeNode(val)
        elif root.val > val:
            if not root.left:
                root.left = TreeNode(val)
            else:
                self.insertIntoBST(root.left, val)
        elif root.val < val:
            if not root.right:
                root.right = TreeNode(val)
            else:
                self.insertIntoBST(root.right, val)

        return root

# 递归法3
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)

        return root


# 迭代法1
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: # 根节点为空
            return TreeNode(val)

        cur = root
        pre = root # 记录上一个节点
        while cur:
            pre = cur
            if cur.val > val:
                cur = cur.left
            else:
                cur = cur.right
        
        node = TreeNode(val)
        if val < pre.val:
            pre.left = node
        else:
            pre.right = node
        
        return root

# 迭代法2
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        pre = None
        cur = root
        while cur:
            pre = cur
            if val < cur.val:
                cur = cur.left
            else:
                cur = cur.right
        if val < pre.val:
            pre.left = TreeNode(val)
        else:
            pre.right = TreeNode(val)

        return root

# 迭代精简法
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: # 根节点为空
            return TreeNode(val)
        cur = root
        while cur:
            if cur.val > val:
                if not cur.left: # 此时节点的左子树为空
                    cur.left = TreeNode(val)
                    return root
                else: # 不为空则继续遍历
                    cur = cur.left
            elif cur.val < val:
                if not cur.right: # 此时节点的右子树为空 
                    cur.right = TreeNode(val)
                    return root
                else: # 不为空则继续遍历
                    cur = cur.right
