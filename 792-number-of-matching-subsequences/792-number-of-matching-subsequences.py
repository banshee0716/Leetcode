class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def issubseq(s,t):
            stack = []
            for i in t:
                stack.append(i)
            
            n = len(s)
            for i in range(n-1,-1,-1):
                if not stack:
                    return True
                if stack[-1] == s[i]:
                    stack.pop()
            return stack == []
        
        
        hashmap = {}
        
        count = 0
        for word in words:
            if word not in hashmap:
                if issubseq(s,word):
                    count += 1
                    hashmap[word] = True
                else:
                    hashmap[word] = False
            else:
                if hashmap[word]:
                    count += 1
        return count