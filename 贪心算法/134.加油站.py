class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cur_sum = 0 # 当前累计的剩余油量
        total_sum = 0   # 总剩余油量
        start_idx = 0   # 起始位置

        for i in range(len(gas)):
            cur_sum += gas[i] - cost[i]
            total_sum += gas[i] - cost[i]

            if cur_sum < 0: # 当前累计剩余油量小于0
                start_idx = i + 1   # 起始位置更新为i+1
                cur_sum = 0 # cur_sum重新累加
        
        if total_sum < 0:   # 总剩余油量小于0，说明无法环绕一圈
            return -1
        return start_idx
