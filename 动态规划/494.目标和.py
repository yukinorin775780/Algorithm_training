# 二维dp数组
class Solution:
    # 假设 left组合为正数集，right组合为负数集
    # left - right = target    
    # left + right = sum => right = sum - left
    # left - (sum - left) = target ==> left = (target + sum) / 2
    # 问题转换成 用nums装满背包容量为left的背包有多少种方法
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        1. 确定dp数组含义: dp[i][j]表示使用下标为[0,i]的nums[i]能够凑满容量为j的背包，有dp[i][j]中方法
        2. 确定递推公式: 不放物品i，dp[i-1][j]中方法；放物品i，dp[i-1][j-物品i容量] ==>
                       dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i]]
        3. dp数组初始化: 初始化第一行和第一列 dp[0][nums[i]] = 1;
        4. 确定遍历顺序: 先物品后背包/先背包后物品
        5. 打印dp数组
        """
        total_sum = sum(nums)
        if abs(target) > total_sum:
            return 0
        if (target + total_sum) % 2 == 1:
            return 0
        target_sum = (target + total_sum) // 2  # 目标和

        dp = [[0] * (target_sum + 1) for _ in range(len(nums) + 1)]

        dp[0][0] = 1

        for i in range(1, len(nums) + 1):
            for j in range(target_sum+1):
                if nums[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
        
        return dp[len(nums)][target_sum]


# 一维dp数组
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        if abs(target) > total_sum:
            return 0
        if (target + total_sum) % 2 == 1:
            return 0
        target_sum = (target + total_sum) // 2
        dp = [0] * (target_sum + 1)
        dp[0] = 1
        for num in nums:
            for j in range(target_sum, num - 1, -1):
                dp[j] += dp[j-num]

        return dp[target_sum]

      
# 回溯算法
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if target > total:
            return 0
        if (target + total) % 2 != 0:
            return 0
        bag_size = (target + total) // 2    # 转化为组合总和问题，bag_size即目标和
        
        result = []
        nums.sort()    # 需要对nums数组排序
        self.backtracking(nums, bag_size, 0, 0, [], result)
        return len(result)
    
    def backtracking(self, candidates, target, total, start_index, path, result):
        if total == target:
            result.append(path[:]) # 将当前路径的副本添加到结果中
        
        for i in range(start_index, len(candidates)):
            # 如果 sum + cnadidate[i] > target，则停止遍历
            if total + candidates[i] > target:
                break
            total += candidates[i]
            path.append(candidates[i])
            self.backtracking(candidates, target, total, i + 1, path, result)
            total -= candidates[i]
            path.pop()
