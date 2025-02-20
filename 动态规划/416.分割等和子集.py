# 一维
class Solution:
    # 抽象成01背包问题————集合内元素能否 装满 大小为sum(nums)/2 的背包
    # 数组内元素的重量和价值相等，都是nums[i]
    def canPartition(self, nums: List[int]) -> bool:
        """
        1. 确定dp数组的含义：dp[j]表示容量为j的背包，所背的物品价值最大为dp[j]
        2. 确定递推公式：dp[j] = max(dp[j], dp[j-weight[i]] + value[i]])
        3. dp数组初始化：dp[j] = 0
        4. 确定遍历顺序：先物品后倒叙遍历背包
        5. 打印dp数组
        """
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        target_sum = total_sum // 2
        dp = [0] * (target_sum + 1)
        for num in nums:
            for j in range(target_sum, num-1, -1):
                dp[j] = max(dp[j], dp[j-num] + num)

        return dp[target_sum] == target_sum


# 二维
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        target = total_sum // 2
        dp = [[0] * (target + 1) for _ in range(len(nums))]

        for j in range(nums[0], target + 1):
            dp[0][j] = nums[0]
        
        for i in range(1, len(nums)):
            for j in range(target + 1):
                if j < nums[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-nums[i]] + nums[i])
        
        return dp[len(nums) - 1][target] == target
