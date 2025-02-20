"""
1. 确定dp数组的含义：dp[j]表示容量为j的背包，所背的物品价值最大为dp[j]
2. 确定递推公式：dp[j] = max(dp[j], dp[j-weight[i]] + value[i])
3. dp数组初始化：dp[j] = 0
4. 确定遍历顺序：先物品后倒叙遍历背包————防止物品重复添加
5. 打印dp数组
"""
dp = [0] * (bagweight + 1)
dp[0] = 0

for i in range(n):  # 先遍历物品
  for j in range(bagweight,weight[i]-1,-1):  # 倒叙遍历背包
    dp[j] = max(dp[j], dp[j-weight[i]] + value[i])

return dp[bagweight]
