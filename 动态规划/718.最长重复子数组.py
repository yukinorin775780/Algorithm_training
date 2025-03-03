class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        """
        1. 确定dp数组含义: dp[i][j]表示以下标i-1为结尾的A和以下标j-1为下标的B，最长重复子数组长度为dp[i][j]
        2. 确定递推公式: if nums[i] == nums[j]: dp[i][j] = dp[i-1][j-1] + 1
        3. dp数组初始化: dp[i][0], dp[0][j]无意义 = 0，其余地方都为 0
        4. 确定遍历顺序: 外层遍历A内层循环遍历B / 外层遍历B内层循环遍历A
        5. 打印dp数组
        """
        # 创建一个二维dp数组，用于存储最长公共子数组的长度
        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        # 记录最长公共子数组的长度
        result = 0

        # 遍历数组nums1
        for i in range(1, len(nums1) + 1):
            # 遍历数组nums2
            for j in range(1, len(nums2) + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > result:
                    result = dp[i][j]
        
        return result
