class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for item in s:
            if not stack or stack[-1] != item:
                stack.append(item)
            else:
                stack.pop()
        return "".join(stack)
