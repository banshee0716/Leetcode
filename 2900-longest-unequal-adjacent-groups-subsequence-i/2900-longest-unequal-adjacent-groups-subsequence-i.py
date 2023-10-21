class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        ans, cur_group = [], -1
        for word, group in zip(words, groups):
            if group != cur_group:
                ans.append(word)
                cur_group = group
                
        return ans
        
        
    """
給您一個整數n，一個0索引的字符串數組單詞和一個0個索引的二進制數組組，兩個數組均具有長度n。

您需要從一系列索引[0，1，...，n -1]中選擇最長的子序列，以使其具有長度為k的子序列表示為[I0，I1，...，.. .，...，IK -1]組[ij]！=組[ij + 1]，每個j其中0 <j + 1 <k。

返回包含與所選子序列中索引（按順序）相對應的單詞的字符串數組。如果有多個答案，請返回其中任何答案。

數組的子序列是一個新數組，它是由原始數組形成的新數組，它通過刪除某些（可能沒有）的元素而不干擾其餘元素的相對位置。

注意：單詞的字符串的長度可能不平等。
    """