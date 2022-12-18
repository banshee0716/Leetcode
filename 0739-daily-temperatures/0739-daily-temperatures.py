class Solution:
    def dailyTemperatures(self, T):
        # Concept = This is similar to having a monotonous stack and you should start
        # the back of array as then you already know how many warmer days are there next
        # to this one and keep going back computing the top of the stack to current temp
        
        res = [0] * len(T)
        stack = []
        
        for index in range(len(T)-1, -1, -1):
            
            while stack and T[stack[-1]] <= T[index]:
                stack.pop()
                        
            res[index] = stack[-1] - index if stack else 0
            
            stack.append(index)

            
        return res 
        
        # return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.