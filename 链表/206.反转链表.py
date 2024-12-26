#双指针
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        pre = None
        while cur:
            temp = cur.next # 保存 cur的下一个节点，因为接下来要改变cur.next（翻转）
            cur.next = pre # 翻转
            pre = cur
            cur = temp
        return pre

#递归
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverse(head, None) 
    def reverse(self, cur: ListNode, pre: ListNode) -> ListNode:
        if cur == None: # 递归结束条件
            return pre
        temp = cur.next 
        cur.next = pre
        return self.reverse(temp, cur)
