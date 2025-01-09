# 递归法
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node):
            if node is None:
                return
            
            res.append(node.val) # 中
            dfs(node.left) # 左
            dfs(node.right) # 右
        
        dfs(root)
        return res

# 迭代法
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 根节点为空返回空列表
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            # 中节点先处理
            result.append(node.val)
            # 右子树先入栈
            if node.right:
                stack.append(node.right)
            # 左子树再入栈
            if node.left:
                stack.append(node.left)
        return result
