class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        path = []
        if not root:
            return result
        self.traversal(root, path, result)
        return result

    def traversal(self, cur, path, result):
        path.append(cur.val) # 中
        if not cur.left and not cur.right: # 到达叶子结点
            s_path = '->'.join(map(str, path))
            result.append(s_path)
            return
        if cur.left: # 左
            self.traversal(cur.left, path, result)
            path.pop() # 回溯
        if cur.right: # 右
            self.traversal(cur.right, path, result)
            path.pop() # 回溯

# 迭代版
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        stack, path_st, result = [root], [str(root.val)], []

        while stack:
            cur = stack.pop()
            path = path_st.pop()
            # 如果当前节点为叶子结点，添加路径到结果中
            if not (cur.left or cur.right):
                result.append(path)
            if cur.right:
                stack.append(cur.right)
                path_st.append(path + '->' + str(cur.right.val))
            if cur.left:
                stack.append(cur.left)
                path_st.append(path + '->' + str(cur.left.val))
        
        return result
