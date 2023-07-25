class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []
        for word in words:
            for each_word in word.split(separator):
                if each_word:
                    ans.append(each_word)
                    
        return ans
                