class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        stack = [0]

        for i in range(1, len(nums2)):
            if nums2[i] <= nums2[stack[-1]]:
                stack.append(i)
            else:
                while len(stack) != 0 and nums2[i] > nums2[stack[-1]]:
                    # 在nums1中找到栈顶元素对应的idx
                    if nums2[stack[-1]] in nums1:
                        idx = nums1.index(nums2[stack[-1]])
                        res[idx] = nums2[i]
                    stack.pop()
                stack.append(i)
        
        return res
