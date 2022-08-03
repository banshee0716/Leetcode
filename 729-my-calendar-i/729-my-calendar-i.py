from sortedcontainers import SortedList

class MyCalendar:
    def __init__(self):
        self.books = SortedList([(float('-inf'), float('-inf')), (float('inf'), float('inf'))])

    def book(self, start: int, end: int) -> bool:
        idx = self.books.bisect_left((start, end))
        if start < self.books[idx-1][1] or end > self.books[idx][0]:
            return False
        self.books.add((start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)