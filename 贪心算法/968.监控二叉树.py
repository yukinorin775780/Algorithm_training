class Solution:
    """
    贪心算法逻辑：从下往上安装摄像头，先给 leaves 的父节点安装摄像头，直到root节点
    0: 该节点未覆盖
    1: 该节点有摄像头
    2: 该节点有覆盖
    """

    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        result = [0]    # 用于记录摄像头的安装数量
        if self.traversal(root, result) == 0:
            result[0] += 1
        
        return result[0]

    def traversal(self, cur: TreeNode, result: List[int]) -> int:
        # 当前节点是空节点，即当前节点父节点是叶子节点，将其状态设置为2，使其父节点不受影响
        if not cur:
            return 2
        # 后序遍历
        # 左
        left = self.traversal(cur.left, result)
        # 右
        right = self.traversal(cur.right, result)
        # 中
        # 情况1: 左右节点都有覆盖
        if left == 2 and right == 2:
            return 0
        # 情况2: 存在某个节点无覆盖
        if not left or not right:
            result[0] += 1
            return 1
        # 情况3: 存在某个节点有摄像头
        if left == 1 or right == 1:
            return 2
