class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        
        steps = 0
        factor = 2
        while n > 1:
            while n % factor == 0:
                steps += factor
                n //= factor
            factor += 1
            
        return steps
            
        
        
        
        
        """
記事本的螢幕上只有一個字元「A」。您可以在此記事本上為每個步驟執行以下兩個操作之一：

全部複製：您可以複製螢幕上出現的所有字元（不允許部分複製）。
貼上：可以貼上上次複製的字元。
給定一個整數 n，傳回螢幕上剛好出現 n 次字元「A」所需的最少操作次數。
        """