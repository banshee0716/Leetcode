class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix = [0]
        for n in nums:
            prefix.append(prefix[-1] + n)#prefix:重新設計一個,陣列中每一個值都是前面加總的陣列
        
        ans = []
        for i in queries:
            ans.append(bisect.bisect(prefix, i) - 1)
        
        return ans
        
        
        #把前面的數字都加起來稱為prefix sum。可以用來解區段和的問題。