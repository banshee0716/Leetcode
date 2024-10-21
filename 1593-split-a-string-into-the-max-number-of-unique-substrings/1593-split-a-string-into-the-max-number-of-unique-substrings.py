class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        self.max_count = 0
        used_substrings = set()
        
        def backtrack(start):
            # 剪枝
            if len(used_substrings) + (len(s) - start) <= self.max_count:
                return
            
            if start == len(s):
                self.max_count = max(self.max_count, len(used_substrings))
                return
            
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if substring not in used_substrings:
                    used_substrings.add(substring)
                    backtrack(end)
                    used_substrings.remove(substring)
        
        backtrack(0)
        return self.max_count
