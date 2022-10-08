class Node(object):
    def __init__(self, start, end, ktime=1):
        self.k = ktime
        self.s = start
        self.e = end
        self.right = None
        self.left = None
        
class MyCalendarThree(object):

    def __init__(self):
        self.root = None
        self.k = 0

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int
        """
        self.root = self.insert(self.root, start, end, 1)
        return self.k
    def insert(self, root, start, end, k):
        if start >= end:
            return root
        if not root:
            self.k = max(self.k, k)
            return Node(start, end, k)
        else:
            if start >= root.e:
                root.right = self.insert(root.right, start, end, k)
                return root
            elif end <= root.s:
                root.left = self.insert(root.left, start, end, k)
                return root
            else:
                
                a = min(root.s, start)
                b = max(root.s, start)
                c = min(root.e, end)
                d = max(root.e, end)
                
                root.left = self.insert(root.left, a, b, a == root.s and root.k or k)
                root.right = self.insert(root.right, c,d, d == root.e and root.k or k)
                root.k += k
                root.s = b
                root.e = c
                self.k = max(root.k, self.k)
                return root
                

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)