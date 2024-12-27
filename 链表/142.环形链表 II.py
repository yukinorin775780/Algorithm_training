# 快指针速度为2，慢指针速度为1，当进入环中，快指针相对于慢指针的速度为1，所以一定能相遇
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            # 如果有环，必定相遇
            if(fast == slow):
                # 此时 设x为出发点到环的起点的距离，y为慢指针在环中移动的距离，z为环的剩余长度
                # 由此可得 2(x+y) = x+y+n(y+z) => x=(n-1)(y+z)+z => 当n=1时，x=z
                index1 = fast # 相遇点到环起点的距离 z
                index2 = head # 头节点到环起点的距离 x
                while index1 != index2:
                    index1 = index1.next
                    index2 = index2.next
            # 当index1 == index2时，说明在起点处相遇
                return index1
        return None
