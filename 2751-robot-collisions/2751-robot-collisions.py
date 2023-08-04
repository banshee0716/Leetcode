class Solution:
    def survivedRobotsHealths(self, positions: List[int], h: List[int], directions: str) -> List[int]:
        
        n = len(positions)
        ind = sorted(range(n), key=positions.__getitem__)
        print(ind)
        stack = []
        for i in ind:
            if directions[i] == "R":
                stack.append(i)
                continue
            while stack and h[i]>0:
                if h[stack[-1]] < h[i]:
                    h[stack.pop()] = 0
                    h[i] -= 1
                elif h[stack[-1]] > h[i]:
                    h[stack[-1]] -= 1     
                    h[i] = 0
                else:
                    h[stack.pop()] = 0
                    h[i] = 0 
                    
        return [v for v in h if v > 0]
    

    """
    維護一個stack，藉此去處理彼此元素彼此之間的碰撞關係
    """