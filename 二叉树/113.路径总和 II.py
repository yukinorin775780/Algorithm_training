# 递归法
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.result = []
        self.path = []
        if not root:
            return self.result
        self.path.append(root.val) # 把根节点放进路径
        self.traversal(root, targetSum - root.val)
        return self.result

    def traversal(self, node, num):
        # 叶子节点且和为sum的路径
        if not node.left and not node.right and num == 0:
            self.result.append(self.path[:])
            return
        
        if node.left:
            self.path.append(node.left.val)
            num -= node.left.val
            self.traversal(node.left, num) # 递归
            num += node.left.val # 回溯
            self.path.pop() # 回溯
        if node.right:
            self.path.append(node.right.val)
            num -= node.right.val
            self.traversal(node.right, num) # 递归a
            num += node.right.val # 回溯
            self.path.pop() # 回溯
        
        return

# 递归精简版
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        self.traversal(root, targetSum, [], result)
        return result
    
    def traversal(self, node, count, path, result):
        if not node:
            return
        path.append(node.val)
        count -= node.val
        if not node.left and not node.right and count == 0:
            result.append(list(path))
        self.traversal(node.left, count, path, result)
        self.traversal(node.right, count, path, result)
        path.pop()

# 迭代法
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        stack = [(root, [root.val])]
        result = []
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right and sum(path) == targetSum:
                result.append(path)
            if node.right:
                stack.append((node.right, path + [node.right.val]))
            if node.left:
                stack.append((node.left, path + [node.left.val]))
        return result
