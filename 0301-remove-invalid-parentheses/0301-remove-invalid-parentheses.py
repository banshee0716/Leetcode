class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        #Calculate the number of unmatched left and right 

        redundant_open=0
        redundat_close=0
        
        for i in s:
            if i=="(":
                redundant_open+=1
            elif i==")":
                if redundant_open>0:
                    redundant_open-=1
                else:
				        # If we don't have a matching left, then this is a misplaced right, record it.

                    redundat_close+=1
        
        ans=set()
        
        def dfs(index,left,right,ope,close,valid):
		    # If we reached the end of the string, just check if the resulting expression is
            # valid or not and also if we have removed the total number of left and right
            # parentheses that we should have removed.
            if index==len(s):
                if left==right and ope==0 and close==0:
                    ans.add(valid)
                return 
            
            if s[index]=='(':
                if ope>0:
                    dfs(index+1,left,right,ope-1,close,valid)
                    
                dfs(index+1,left+1,right,ope,close,valid+"(")
                
            elif s[index]==')':
                if close>0:
                    dfs(index+1,left,right,ope,close-1,valid)
                if  right<left:  
                    dfs(index+1,left,right+1,ope,close,valid+")")
            else:
                dfs(index+1,left,right,ope,close,valid+s[index])
                
                    
                
        dfs(0,0,0,redundant_open,redundat_close,"")
        return list(ans)
     