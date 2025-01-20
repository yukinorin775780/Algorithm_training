# 中序遍历-数组
class Solution:
    def __init__(self):
        self.vec = []
        
    def traversal(self, root):
        if not root:
            return 
        self.traversal(root.left) # 左
        self.vec.append(root.val) # 中，将二叉搜索树转换成有序数组
        self.traversal(root.right)

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.vec = []
        self.traversal(root)
        if len(self.vec) < 2:
            return 0
        
        result = float('inf')
        for i in range(1, len(self.vec)):
            # 统计有序数组最小差值
            result = min(result, self.vec[i] - self.vec[i-1])
        
        return result

# 中序遍历-pre
class Solution:
    def __init__(self):
        self.result = float('inf')
        self.pre = None

    def traserval(self, cur):
        if not cur:
            return
        self.traserval(cur.left) # 左
        # 中
        if self.pre:
            self.result = min(self.result, cur.val - self.pre.val)
        self.pre = cur
        self.traserval(cur.right) # 右 

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.traserval(root)
        return self.result

# 迭代法
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        stack = []
        cur = root
        pre = None
        result = float('inf')

        while cur or len(stack) > 0:
            if cur:
                stack.append(cur) # 将访问的节点放进栈
                cur = cur.left # 左
            else:
                cur = stack.pop()
                if pre:
                    result = min(result, cur.val - pre.val)
                pre = cur
                cur = cur.right # 右
            
        return result

