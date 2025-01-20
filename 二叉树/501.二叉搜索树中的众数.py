# 递归 + 字典
from collections import defaultdict

class Solution:
    def searchBST(self, cur, freq_map):
        if not cur:
            return 
        freq_map[cur.val] += 1 #统计各元素频率
        self.searchBST(cur.left, freq_map)
        self.searchBST(cur.right, freq_map)

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        freq_map = defaultdict(int) # key:元素，value:出现的频率
        result = []
        if not root:
            return result
        self.searchBST(root, freq_map)
        max_freq = max(freq_map.values())
        for key, freq in freq_map.items():
            if freq == max_freq:
                result.append(key)
        return result

#中序遍历 + 利用count和max_count
class Solution:
    def __init__(self):
        self.max_count = 0 # 最大频率
        self.count = 0 # 统计频率
        self.pre = None
        self.result = []

    def searchBST(self, cur):
        if not cur:
            return 
        
        self.searchBST(cur.left) # 左
        
        # 中
        if not self.pre: # 第一个节点
            self.count = 1
        elif self.pre.val == cur.val: # 与前一个节点数值相同
            self.count += 1
        else: # 与前一个节点数值不同
            self.count = 1
        self.pre = cur

        if self.count == self.max_count: # 如果与最大频率相同，放入result
            self.result.append(cur.val)
        
        if self.count > self.max_count: # 如果频率大于最大频率
            self.max_count = self.count # 更新最大频率
            self.result = [cur.val] # 清空result并记录新的值
    

        self.searchBST(cur.right) # 右
        return

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.count = 0
        self.max_count = 0
        self.pre = None
        self.result = []

        self.searchBST(root)
        
        return self.result


# 迭代法
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        st = []
        cur = root
        pre = None
        max_count = 0
        count = 0
        result = []

        while cur or st:
            if cur: #指针来访问节点，访问到最底层
                st.append(cur) # 将访问的节点放入栈
                cur = cur.left  # 左
            else:
                cur = st.pop()
                if not pre: # 第一个节点
                    count = 1
                elif pre.val == cur.val: # 与前一个节点数值相同
                    count += 1
                else: # 与前一个节点数值不同
                    count = 1
                
                if count == max_count: # 和最大频率相同，放进result中
                    result.append(cur.val)
                
                if count > max_count:
                    max_count = count # 更新最大频率
                    result = [cur.val] # 清空result数组并放入新值
                
                pre = cur
                cur = cur.right # 右

        return result
