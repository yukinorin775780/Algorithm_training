class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        cur_distance = 0    # 当前覆盖最远距离下标
        step = 0    # 记录走的最大步数
        next_distance = 0   # 下一步覆盖最远距离下标

        for i in range(len(nums)):
            next_distance = max(nums[i] + i, next_distance) # 更新下一步覆盖的最远距离下标
            if i == cur_distance:   # 到达当前覆盖最远距离下标
                step += 1   # 需要走下一步
                cur_distance = next_distance    # 更新当前覆盖最远距离下标
                if next_distance >= len(nums) - 1:  # 当前覆盖最远距离到达数组末尾，返回step
                    break
        
        return step
