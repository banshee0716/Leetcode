class ListNode:
    def __init__(self, val: int, nxt: ListNode = None):
        self.val = val
        self.next = nxt

class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.maxSize = k
        self.size = 0
        self.head = None
        self.tail = None
        
    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull(): 
            return False
        newNode = ListNode(value)
        if self.isEmpty() :
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = self.tail.next
        self.size += 1
        
        return True

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.head = self.head.next
        self.size -= 1
        return True

    def Front(self):
        """
        :rtype: int
        """
        return -1 if self.isEmpty() else self.head.val
    def Rear(self):
        """
        :rtype: int
        """
        return -1 if self.isEmpty() else self.tail.val

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.size == 0

    def isFull(self):
        """
        :rtype: bool
        """
        return self.size == self.maxSize


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()