# 使用递归
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.compare(root.left, root.right)
    
    def compare(self, left, right):
        # 排除空节点情况
        if not left and right:
            return False
        elif left and not right:
            return False
        elif not left and not right:
            return True
        # 排除空节点后，再排除数值不相同的情况
        elif left.val != right.val:
            return False
        
        # 此时就是，左右节点都不为空且数值相同
        # 此时才做递归，做下一层判断
        outside = self.compare(left.left, right.right) # 左子树的左/右子树的右
        inside = self.compare(left.right, right.left) # 左子树的右/右子树的左
        isSame = outside and inside # 左子树的中/右子树的中
        return isSame
 
# 使用队列
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        queue = collections.deque()

        queue.append(root.left) # 将左子树头节点加入队列
        queue.append(root.right) # 将右子树头节点加入队列
        while queue:
            leftNode = queue.popleft()
            rightNode = queue.popleft()
            if not leftNode and not rightNode: # 左右节点为空时是对称的
                continue
            
            # 左右一个节点不为空，或者都不为空但数值不同时，返回false
            if not leftNode or not rightNode or leftNode.val != rightNode.val:
                return False
            
            queue.append(leftNode.left) 
            queue.append(rightNode.right)
            queue.append(leftNode.right)
            queue.append(rightNode.left)
        
        return True

# 使用栈
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        stack = []
        stack.append(root.left)
        stack.append(root.right)
        while stack:
            rightNode = stack.pop()
            leftNode = stack.pop()
            
            if not leftNode and not rightNode:
                continue
            
            if not leftNode or not rightNode or leftNode.val != rightNode.val:
                return False

            stack.append(leftNode.left)
            stack.append(rightNode.right)
            stack.append(leftNode.right)
            stack.append(rightNode.left)

        return True 

# 层寻遍历
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        queue = collections.deque([root.left, root.right])

        while queue:
            level_size = len(queue)

            if level_size % 2 != 0:
                return False
            
            level_vals = []
            for i in range(level_size):
                cur = queue.popleft()
                if cur:
                    level_vals.append(cur.val)
                    queue.append(cur.left)
                    queue.append(cur.right)
                else:
                    level_vals.append(None)
            # 层序遍历当前层的数值是否回文
            if level_vals != level_vals[::-1]:
                return False
        
        return True
