class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = collections.deque([root])
        result = []

        while queue:
            level_size = len(queue)

            for i in range(level_size): 
                cur = queue.popleft()
                if i == level_size - 1: # 层序遍历到每层的最后输出
                    result.append(cur.val)

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return result
