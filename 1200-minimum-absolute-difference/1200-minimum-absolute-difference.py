class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        abs_different = float('inf')
        res = []
        for i in range(1, len(arr)):
            prev = arr[i-1]
            curr= abs(arr[i]-arr[i-1])
            if curr < abs_different:
                res = [[prev, arr[i]]]
                abs_different = curr
            elif curr == abs_different:
                res.append([prev,arr[i]])
        
        return res