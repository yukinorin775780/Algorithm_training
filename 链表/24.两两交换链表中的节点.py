class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(next=head)
        cur = dummy_head
        # 必须有cur的下一个 和 下下个才能交换，否则说明交换已经结束
        while cur.next and cur.next.next:
            temp = cur.next # 防止节点修改
            temp1 = cur.next.next.next

            cur.next = cur.next.next
            cur.next.next = temp
            temp.next = temp1
            cur = cur.next.next
        return dummy_head.next
