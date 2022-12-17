class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        n = len(tokens)
        mark = ["+", "-", "*", "/"]
        for i in tokens:
            if i in mark :
                b = stack.pop()
                a = stack.pop()
                
                if i == "+":
                    stack.append(int(a+b))
                if i == "-":
                    stack.append(int(a-b))
                if i == "*":
                    stack.append(int(a*b))
                if i == "/":
                    stack.append(int(a/b))
                    
            else:
                stack.append(int(i))
        
        return int(stack[0])
            

            
            
            
            
            
            
            


