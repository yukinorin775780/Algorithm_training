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
