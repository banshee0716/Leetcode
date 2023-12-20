class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        return money-sum(heapq.nsmallest(2, prices)) if money-sum(heapq.nsmallest(2, prices))>= 0 else money