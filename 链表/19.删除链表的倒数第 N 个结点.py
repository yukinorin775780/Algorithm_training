# 快慢指针实现一步遍历
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 创建一个虚拟头节点，并将其下一个指针设置为链表的头部
        dummy_head = ListNode(next = head)
        # 创建两个指针，慢指针和快指针，同时指向虚拟头节点
        fast = dummy_head
        slow = dummy_head
        # 快指针比慢指针多走 n+1 步
        for _ in range(n+1):
            fast = fast.next
        # 同时移动两个指针，直到快指针到达链表末尾
        while fast:
            fast = fast.next
            slow = slow.next
        # 通过更新第 (n-1) 个节点的next指针来删除第 n 个节点
        slow.next = slow.next.next

        return dummy_head.next
