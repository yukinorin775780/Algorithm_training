"""
1. 确定dp数组的含义:dp[i][j]表示从下标为[0-i]的物品里任意取，放进容量为j的背包，价值总和最大是dp[i][j]
2. 确定递推公式:  不放物品i:dp[i-1][j], 放物品i: dp[i-1][j-weight[i]] + value[i] ==> 
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]] + value[i] )
3. dp数组初始化： 背包容量为0时，即 dp[i][0] = 0; 放入物品0时，即dp[0][j] = value[0]
4. 确定遍历顺序： 先物品后背包/先背包后物品
5. 打印dp数组
"""

dp = [[0] * (bagweight + 1) for _ in range(n)]

for j in range(weight[0], bagweight + 1):
  dp[0][j] = value[0]

for i in range(1, n):
  for j in range(bagweight + 1):
    if j < weight[i]:
      dp[i][j] = dp[i-1][j]
    else:
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]] + value[i])

return dp[n-1][bagweight]
