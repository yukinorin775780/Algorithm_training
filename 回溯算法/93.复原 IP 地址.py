# 回溯版本1
class Solution:
    def backtracking(self, s, start_index, point_num, current, result):
        if point_num == 3:  # 逗点数量为3时，分割结束
            if self.isVaild(s, start_index, len(s)-1): #判断第四段字符串是否合法
                current += s[start_index:] # 添加最后一段子字符串
                result.append(current)
            return
        
        for i in range(start_index, len(s)):
            if self.isVaild(s, start_index, i): # 判断 [start_index, i] 这个区间的子串是否合法
                sub = s[start_index: i+1]
                self.backtracking(s, i+1, point_num+1, current + sub + '.', result)
            else:
                break

    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        self.backtracking(s, 0, 0, "", result)
        return result

    def isVaild(self, s, start, end):
        if start > end:
            return False
        if s[start] == '0' and start != end:    # 0开头不合法
            return False
        num = 0
        for i in range(start, end + 1):
            if not s[i].isdigit():  # 非数字不合法
                return False
            num = num * 10 + int(s[i])
            if num > 255: # 数字大于255不合法
                return False
        return True

# 回溯版本2
class Solution:
    def backtracking(self, s, index, path, result):
        if index == len(s) and len(path) == 4:
            result.append('.'.join(path))
            return
        
        if len(path) > 4:   # 剪枝
            return

        for i in range(index, min(index + 3, len(s))):
            if self.isVaild(s, index, i):
                sub = s[index: i+1]
                path.append(sub)
                self.backtracking(s, i+1, path, result)
                path.pop()

    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        self.backtracking(s, 0, [], result)
        return result

    def isVaild(self, s, start, end):
        if start > end:
            return False
        if s[start] == '0' and start != end:    # 0开头不合法
            return False
        num = int(s[start:end+1])
        return 0 <= num <= 255

# 回溯版本3
class Solution:
    def backtracking(self, s, index, path, result):
        if index == len(s):
            result.append('.'.join(path))
            return

        for i in range(index, min(index + 3, len(s))):
            # 如果 i 往后遍历了，并且当前位置的第一个元素为 0，就直接退出
            if i > index and s[index] == '0':
                break
            """
            比如 s 长度为 5，当前遍历到 i = 3 这个元素
            因为还没有执行任何操作，所以此时剩下的元素数量就是 5 - 3 = 2，即包括当前 i 的本身
            path 里面是当前包含的子串，所以有几个元素就表示存放了几个地址
            所以 4 - len(path) * 3 表示当前路径至多能存放的元素个数
            4 - len(path) 表示至少要存放多少个元素
            """
            if (4 - len(path)) * 3 < len(s) - i or 4 - len(path) > len(s) - i:
                break
            
            if i - index == 2:
                if not int(s[index:i+1]) <= 255:
                    break
            path.append(s[index:i+1])
            self.backtracking(s, i+1, path, result)
            path.pop()

    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        self.backtracking(s, 0, [], result)
        return result
            
