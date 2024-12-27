# 求链表长度，同时出发
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA, lenB = 0, 0
        cur = headA
        #求链表A长度
        while cur:
            cur = cur.next
            lenA +=1
        cur = headB
        #求链表B长度
        while cur:
            cur = cur.next
            lenB +=1
        curA, curB = headA, headB
        if lenA > lenB:
            #让 curB 为最长链的头，lenB为其长度
            curA, curB = curB, curA
            lenA, lenB = lenB, lenA
        for _ in range(lenB - lenA):
            # 让 curA 和 curB 在同一起点（末尾位置对齐）
            curB = curB.next
        while curA: #遍历curA，curB，遇到相同则直接返回
            if curA == curB:
                return curA
            else:
                curA = curA.next
                curB = curB.next

        return None
