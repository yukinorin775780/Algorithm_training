class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        
        queue = collections.deque([root])
        averages = []

        while queue:
            size = len(queue)
            level_sum = 0
            for i in range(size):
                cur = queue.popleft()
                level_sum += cur.val # 层序遍历节点求和

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            
            averages.append(level_sum / size) # 当前层结束后求平均

        return averages
