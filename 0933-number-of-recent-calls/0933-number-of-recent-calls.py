class RecentCounter:

    def __init__(self):
        self.ls = []
        

    def ping(self, t: int) -> int:
        self.ls.append(t)
        return len(self.ls) - bisect.bisect_left(self.ls, t - 3000)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)