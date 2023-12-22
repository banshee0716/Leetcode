class Solution:
    def maxScore(self, s: str) -> int:
        max_score = count_zeros_left = 0
        count_ones_right = s.count('1')
        
        for i in range(len(s)-1):
            count_zeros_left += s[i] == "0"
            count_ones_right -= s[i] == '1'
            max_score = max(max_score, count_zeros_left + count_ones_right)
        
        return max_score
            
        
    
    
    """
給定一個由 0 和 1 組成的字串 s，將字串拆分為兩個非空子字串（即左子字串和右子字串）後傳回最大分數。

分割字串後的分數是左子字串中 0 的數量加上右子字串中 1 的數量。
    """