class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 统计元素出现的频率
        map_ = {}
        for i in range(len(nums)):
            map_[nums[i]] = map_.get(nums[i], 0) + 1
        
        # 对频率排序,定义一个小顶堆，大小为k
        pri_que = []

        # 用固定大小为k的小顶堆，扫描所有频率的数值
        for key, freq in map_.items():
            heapq.heappush(pri_que, (freq, key))
            if len(pri_que) > k: # 堆的大小大于k，弹出队列
                heapq.heappop(pri_que)
        
        result = [0] * k
        for i in range(k-1, -1, -1):
            result[i] = heapq.heappop(pri_que)[1]
        return result
