# 数组
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = [0] * 1001
        count2 = [0] * 1001
        result = []
        for i in range(len(nums1)):
            count1[nums1[i]] += 1
        for i in range(len(nums2)):
            count2[nums2[i]] += 1
        for i in range(1001):
            if count1[i] * count2[i] > 0:
                result.append(i)
        return result

# 使用字典和集合
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 使用哈希表存储一个数组中的所有元素
        table = {}
        for num in nums1:
            table[num] = table.get(num, 0) + 1
        
        # 使用集合存储结果
        res = set()
        for num in nums2:
            if num in table:
                res.add(num)
                del table[num]
        
        return list(res)

# 使用集合
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

