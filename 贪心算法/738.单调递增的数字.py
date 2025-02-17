class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        # 将整数转换成字符串方便操作
        str_num = str(n)
        # flag 用来标记赋值为“9”的起始索引
        # 设置为字符串长度，为了防止第二个for循环 在flag没有被赋值的情况下 执行
        flag = len(str_num)

        # 从右往左遍历字符串
        for i in range(len(str_num) - 1, 0, -1):
            # 如果当前字符比前一个字符小，说明需要修改前一个字符
            if str_num[i-1] > str_num[i]:
                # 更新flag的值，记录需要修改的索引
                flag = i
                # 将前一个字符 -1，以保证递增
                str_num = str_num[:i-1] + str(int(str_num[i-1]) - 1) + str_num[i:]
        
        # 将flag索引后的字符都修改为9
        for i in range(flag, len(str_num)):
            str_num = str_num[:i] + '9' + str_num[i+1:]

        return int(str_num)
