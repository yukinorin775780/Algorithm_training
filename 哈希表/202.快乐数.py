# 使用集合1
class Solution:
    def isHappy(self, n: int) -> bool:
        record = set()
        while True:
            n = self.get_sum(n)
            if n == 1:
                return True
            
            # 如果计算过程中出现了出现过的值，那么说明进入了死循环
            if n in record:
                return False
            else:
                record.add(n)
        

    def get_sum(self, n: int) -> int:
        new_num = 0
        while n:
            n, r = divmod(n, 10)
            new_num += r**2
        return new_num

# 使用集合2
class Solution:
    def isHappy(self, n: int) -> bool:
        record = set()
        while n not in record:
            record.add(n)
            new_num = 0
            n_str = str(n)
            for s in n_str:
                new_num += int(s)**2
            if new_num == 1:
                return True
            else:
                n = new_num
        return False

# 使用数组
class Solution:
    def isHappy(self, n: int) -> bool:
        record = []
        while n not in record:
            record.append(n)
            new_num = 0
            n_str = str(n)
            for s in n_str:
                new_num += int(s) **2
            if new_num == 1:
                return True
            else:
                n = new_num
        return False

# 使用快慢指针
class Solution:
    def isHappy(self, n: int) -> bool:
        fast = n
        slow = n
        while self.get_sum(fast) != 1 and self.get_sum(self.get_sum(fast)):
            slow = self.get_sum(slow)
            fast = self.get_sum(self.get_sum(fast))
            # 如果出现重复，则必进入循环，快指针相对于慢指针每次多移动，所以必定会相等
            if slow == fast:
                return False
        return True

    def get_sum(self, n: int) -> int:
        new_num = 0
        while n:
            n, r = divmod(n, 10)
            new_num += r ** 2
        return new_num

# 集合 + 精简
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            n = sum(int(i) ** 2 for i in str(n))
            if n in seen:
                return False
            else:
                seen.add(n)
        return True

# 数组 + 精简
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = []
        while n != 1:
            n = sum(int(i) ** 2 for i in str(n))
            if n in seen:
                return False
            else:
                seen.append(n)
        return True


