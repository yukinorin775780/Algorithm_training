class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)    # 如果数组长度为0或1，则返回数组长度
        cur_diff = 0    # 当前一对元素的差值
        pre_diff = 0    # 前一对元素的差值
        result = 1  # 记录峰值个数，初始为1（默认最右边元素被视为峰值）
        for i in range(len(nums) - 1):
            cur_diff = nums[i + 1] - nums[i]    # 计算当前一对元素的差值
            # 如果遇到一个峰值
            if (pre_diff <= 0 and cur_diff > 0) or (pre_diff >= 0 and cur_diff < 0):
            # 方法2
            # if curDiff * preDiff <= 0 and curDiff !=0:  #差值为0时，不算摆动
                result += 1 # 峰值个数加一
                pre_diff = cur_diff # 只有在出现摆动变化时更新pre_dif
        return result
