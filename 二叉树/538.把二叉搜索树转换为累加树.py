# 递归法
class Solution:
    def traversal(self, cur):
        if not cur:
            return
        self.traversal(cur.right)
        cur.val += self.pre
        self.pre = cur.val
        self.traversal(cur.left)
        
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.pre = 0 # 记录前一个节点的值
        self.traversal(root)
        return root

# 迭代法
class Solution:   
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        stack = []
        result = []
        cur = root
        pre = 0

        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.right
            else:
                cur = stack.pop()
                cur.val += pre
                pre = cur.val
                cur = cur.left
            
        return root
