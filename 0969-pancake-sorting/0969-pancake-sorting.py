class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        l = []
        n = len(arr)
        while n > 0 and sorted(arr) != arr:
            x = arr.index(n) + 1
            z = arr[:x]        
            z.reverse()
            l.append(x)
            arr[:x] = z
            if sorted(arr) == arr:
                break
            z = arr[:n]
            z.reverse()
            arr[:n] = z
            l.append(n)
            n -= 1
        return l