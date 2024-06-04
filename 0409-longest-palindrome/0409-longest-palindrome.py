class Solution:
    def longestPalindrome(self, s: str) -> int:
        letter = {}
        max = 0
        #檢測是否已經在hash中,如果是的話把那個pop出去,然後max += 2(兩側的偶數字母)
        for i in s:
            if i in letter:
                max += 2
                letter.pop(i)
            else:
                letter[i] = 1
        
        if letter: #如果還有剩餘,就挑一個出來當成回文的軸心
            max += 1
        
        return max