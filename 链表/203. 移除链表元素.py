# 使用原来链表操作
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head is not None and head.val == val:
            head = head.next
        
        cur = head
        while cur is not None and cur.next is not None:
            if(cur.next.val == val):
                cur.next = cur.next.next
            else:
                cur = cur.next
        
        return head

# 使用虚拟头节点操作
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 创建虚拟头节点
        dummy_head = ListNode(next = head)

        # 遍历列表并删除值为 val 的节点
        cur = dummy_head
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy_head.next
