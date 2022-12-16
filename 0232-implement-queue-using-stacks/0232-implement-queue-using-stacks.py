class MyQueue:

    def __init__(self):
        self.stack = []
        self.index = 0
        #紀錄stack的屬性

    def push(self, x: int) -> None:
        self.stack.append(x)
        #Pushes element x to the back of the queue.

    def pop(self) -> int:
        self.index += 1
        return self.stack[self.index-1]
        #Removes the element from the front of the queue and returns it.

    def peek(self) -> int:
        return self.stack[self.index]
        # Returns the element at the front of the queue.

    def empty(self) -> bool:
        return self.index >= len(self.stack)
        #Returns true if the queue is empty, false otherwise.


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()