class MyStack:

    def __init__(self):
        self._queue = collections.deque()

    def push(self, x: int) -> None:
        q = self._queue
        q.append(x)
        for i in range(len(q)-1):
            q.append(q.popleft())

    def pop(self) -> int:
        return self._queue.popleft()

    def top(self) -> int:
        return self._queue[0]

    def empty(self) -> bool:
        return not len(self._queue)

        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()