class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n):
            if nums[i] > target and nums[i] > 0 and target > 0: # 剪枝
                break
            if i > 0 and nums[i] == nums[i-1]: # 去重
                continue
            for j in range(i+1, n):
                if nums[i] + nums[j] > target and target > 0: # 剪枝
                    break
                if j > i+1 and nums[j] == nums[j-1]: # 去重
                    continue
                left, right = j+1, n-1
                while left < right:
                    sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if sum == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left+1]: # 去重
                            left += 1
                        while right > left and nums[right] == nums[right-1]: # 去重
                            right -= 1
                        left += 1
                        right -= 1
                    elif sum < target:
                        left += 1
                    else:
                        right -= 1
        return result
