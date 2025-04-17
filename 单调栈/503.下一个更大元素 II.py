# 方法1
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * (2 * len(nums))
        stack = [0]
        # 数组相加模拟循环
        nums2 = nums + nums

        for i in range(1, len(nums2)):
            if nums2[i] <= nums2[stack[-1]]:
                stack.append(i)
            else:
                while len(stack) != 0 and nums2[i] > nums2[stack[-1]]:
                    res[stack[-1]] = nums2[i]
                    stack.pop()
                stack.append(i)
        
        return res[0: len(nums)]

# 方法2
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        stack = [0]

        for i in range(2 * len(nums)):
            # 通过去模的方式模拟循环
            while len(stack) != 0 and nums[i % len(nums)] > nums[stack[-1]]:
                res[stack[-1]] = nums[i % len(nums)]
                stack.pop()

            stack.append(i % len(nums))
        
        return res
