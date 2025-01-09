# 递归法
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node):
            if node is None:
                return

            dfs(node.left)
            dfs(node.right)
            res.append(node.val)
        
        dfs(root)
        return res


# 迭代法
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 根节点为空则返回空列表
        if not root:
            return []
        
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            # 先处理中节点
            result.append(node.val)
            # 左子树先进栈
            if node.left:
                stack.append(node.left)
            # 右子树再进栈
            if node.right:
                stack.append(node.right)
        # 最终将数组反转   前序遍历是 中左右 -(调整代码左右顺序)-> 中右左 -(反转)-> 左右中
        return result[::-1]
