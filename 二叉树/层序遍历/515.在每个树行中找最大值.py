class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = collections.deque([root])
        result = []

        while queue:
            size = len(queue)
            max_val = float('-inf')
            
            for _ in range(size):
                cur = queue.popleft()
                max_val = max(max_val, cur.val)

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            
            result.append(max_val)
        
        return result
