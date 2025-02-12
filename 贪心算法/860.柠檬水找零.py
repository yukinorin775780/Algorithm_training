class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        for i in range(len(bills)):
            # 情况1: 收到5美元
            if bills[i] == 5:
                five += 1

            # 情况2：收到10美元
            if bills[i] == 10:
                if five == 0:
                    return False
                else:
                    ten += 1
                    five -= 1
            # 情况3：收到20美元
            if bills[i] == 20:
                # 先尝试用10美元和5美元找零
                if ten >= 1 and five >= 1:
                    ten -= 1
                    five -= 1
                # 再尝试用3张5美元找零
                elif five >= 3:
                    five -= 3
                else:
                    return False
        
        return True
