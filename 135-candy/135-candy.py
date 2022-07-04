class Solution:
    def candy(self, R):
        n, ans = len(R), [1]*len(R) #先開了各一
        for i in range(n-1):
            if R[i] < R[i+1]:
                ans[i+1] = 1 + ans[i]
        
        for i in range(n-2,-1,-1):
            if R[i+1] < R[i]:
                ans [i] = max(1+ans[i+1],ans[i])
        
        return sum(ans)
                
                
                
                
                
    #評分較高者一定要有比鄰居較多的糖果，先排列是否有比右多，之後比較左是否比右高，兩者互換
                