# 递归-中序遍历-转换成数组
class Solution:
    def __init__(self):
        self.vec = []
    
    def traversal(self, root):
        if not root:
            return None
        self.traversal(root.left)
        self.vec.append(root.val) # 将二叉搜索树转换为有序数组
        self.traversal(root.right)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.vec = []
        self.traversal(root)
        for i in range(1, len(self.vec)):
            if self.vec[i] <= self.vec[i-1]:
                return False
        return True

# 递归-中序遍历-设定极小值
class Solution:
    def __init__(self):
        self.max_val = float('-inf')
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        left = self.isValidBST(root.left)
        if self.max_val < root.val:
            self.max_val = root.val
        else:
            return False
        right = self.isValidBST(root.right)
    
        return left and right

# 递归-中序遍历-pre记录上一个节点
class Solution:
    def __init__(self):
        self.pre = None
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        left = self.isValidBST(root.left)
        if self.pre and self.pre.val >= root.val:
            return False
        self.pre = root # 记录前一个节点

        right = self.isValidBST(root.right)
    
        return left and right

# 迭代法
class Solution:  
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        cur = root
        pre = None # 记录前一个节点
        while cur or len(stack) > 0:
            if cur:
                stack.append(cur)
                cur = cur.left # 左
            else:
                cur = stack.pop() # 中
                if pre and cur.val <= pre.val:
                    return False
                pre = cur # 记录前一个节点
                cur = cur.right # 右
                
        return True
