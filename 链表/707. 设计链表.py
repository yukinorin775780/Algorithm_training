#单链表
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.dummy_head = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        cur_node = self.dummy_head.next
        for i in range(index):
            cur_node = cur_node.next
        
        return cur_node.val

    def addAtHead(self, val: int) -> None:
        self.dummy_head.next = ListNode(val, self.dummy_head.next)
        self.size += 1

    def addAtTail(self, val: int) -> None:
        cur_node = self.dummy_head
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = ListNode(val)
        self.size += 1
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        
        cur_node = self.dummy_head
        for i in range(index):
            cur_node = cur_node.next
        cur_node.next = ListNode(val, cur_node.next)
        self.size += 1
        
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        cur_node = self.dummy_head
        for i in range(index):
            cur_node = cur_node.next
        cur_node.next = cur_node.next.next
        self.size -= 1
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

#双链表
class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        if index < self.size // 2:
            cur_node = self.head
            for i in range(index):
                cur_node = cur_node.next
        else:
            cur_node = self.tail
            for i in range(self.size - index - 1):
                cur_node = cur_node.prev
    
        return cur_node.val

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val, None, self.head)
        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val, self.tail, None)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node
        self.size += 1
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            if index < self.size // 2:
                cur_node = self.head
                for i in range(index-1):
                    cur_node = cur_node.next
            else:
                cur_node = self.tail
                for i in range(self.size - index):
                    cur_node = cur_node.prev
            new_node = ListNode(val, cur_node, cur_node.next)
            cur_node.next.prev = new_node
            cur_node.next = new_node
            self.size += 1
                
        
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
        elif index == self.size - 1:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
        else:
            if index < self.size // 2:
                cur_node = self.head
                for i in range(index):
                    cur_node = cur_node.next
            else:
                cur_node = self.tail
                for i in range(self.size - index - 1):
                    cur_node = cur_node.prev
            cur_node.next.prev = cur_node.prev
            cur_node.prev.next = cur_node.next
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
