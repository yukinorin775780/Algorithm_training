# 题目链接：https://kamacoder.com/problempage.php?pid=1065

# 方法1 
# 获取输入的数字和字符串
k = int(input())
s = input()

s = s[::-1]
s = s[k-1::-1] + s[:k-1:-1]
print(s)

# 方法2
# 获取输入的数字和字符串
k = int(input())
s = input()

s = s[len(s) - k:] + s[:len(s)-k]
print(s)

# 方法3
# 获取输入的数字和字符串
k = int(input())
s = input()

print(s[-k:] + s[:-k])
