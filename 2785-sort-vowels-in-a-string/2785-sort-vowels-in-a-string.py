class Solution:
    def sortVowels(self, s: str) -> str:
        vowels, ans = 'AEIOUaeiou', ''
        sVowels = deque(sorted(filter(
                        lambda x: x in vowels, s)))
        for ch in s:
            if ch in vowels:
                ans += sVowels.popleft()
            else:
                ans += ch
                
        return ans
                
                
                
"""現在，讓我們來解析這段程式碼的每個部分：

lambda x: x in vowels, s：這是一個lambda函數，用於檢查一個字符是否為元音字母。如果字符在元音字母列表中，則返回True，否則返回False。

filter()：這個函數接受兩個參數，第一個是一個函數，第二個是一個序列。它將函數應用於序列的每個元素，並返回一個新的迭代器，只包含使函數返回值為True的元素。在這裡，它用於從字符串s中篩選出所有的元音字母。

sorted()：這個函數將序列的元素排序並返回一個新的列表。在這裡，它用於將篩選出的元音字母排序。

deque()：這個函數將可迭代的對象（在這裡是一個列表）轉換為一個deque對象。在這裡，它用於創建一個包含排序後的元音字母的deque對象。

例如，如果我們的輸入字符串為 "Hello, World!"，並且我們的元音字母列表為 ['a', 'e', 'i', 'o', 'u']，則此段程式碼將返回一個包含 ['e', 'o', 'o'] 的 deque 對象。"""