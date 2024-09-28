class Node:
    def __init__(self, value):
        self.val = value
        self.next = self.pre = None
        
class MyCircularDeque:
    def __init__(self, k):
        self.head = self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.size = k
        self.curSize = 0

    def add(self, value, preNode):
        new = Node(value)
        new.pre = preNode
        new.next = preNode.next
        new.pre.next = new.next.pre = new
        self.curSize += 1
        
    def remove(self, preNode):
        node = preNode.next
        node.pre.next = node.next
        node.next.pre = node.pre
        self.curSize -= 1
    
    def insertFront(self, value):
        if self.curSize < self.size:
            self.add(value, self.head)
            return True
        return False

    def insertLast(self, value):
        if self.curSize < self.size:
            self.add(value, self.tail.pre)
            return True
        return False

    def deleteFront(self):
        if self.curSize:
            self.remove(self.head)
            return True
        return False

    def deleteLast(self):
        if self.curSize:
            self.remove(self.tail.pre.pre)
            return True
        return False

    def getFront(self):
        if self.curSize:
            return self.head.next.val
        return -1

    def getRear(self):
        if self.curSize:
            return self.tail.pre.val
        return -1

    def isEmpty(self):
        return self.curSize == 0

    def isFull(self):
        return self.curSize == self.size
        
        
'''
MyCircularDeque(int k) 以最大大小 k 初始化雙端佇列。
boolean insertFront() 在 Deque 的前面新增一個項目。如果操作成功則傳回 true，否則傳回 false。
boolean insertLast() 在 Deque 的最後加上一個項目。如果操作成功則傳回 true，否則傳回 false。
boolean deleteFront() 從 Deque 的前面刪除一個項目。如果操作成功則傳回 true，否則傳回 false。
boolean deleteLast() 從 Deque 後面刪除一個項目。如果操作成功則傳回 true，否則傳回 false。
int getFront() 傳回雙端佇列中最前面的項目。如果雙端佇列為空，則傳回 -1。
int getRear() 傳回 Deque 中的最後一項。如果雙端佇列為空，則傳回 -1。
boolean isEmpty() 如果雙端佇列為空，則傳回 true，否則傳回 false。
boolean isFull() 如果雙端佇列已滿，則傳回 true，否則傳回 false。
'''

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()