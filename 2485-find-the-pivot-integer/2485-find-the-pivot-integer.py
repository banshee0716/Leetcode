class Solution:
    def pivotInteger(self, n: int) -> int:
        x = sqrt(n*(n + 1) / 2)
        if x % 1 != 0:
            return -1
        
        return int(x)
            
        
    
    
    """
給定一個正整數 n，求主元整數 x，使得：

1 到 x 之間所有元素的總和等於 x 到 n 之間所有元素的總和（包括 x 和 n）。
傳回主元整數 x。如果不存在這樣的整數，則傳回-1。保證給定輸入最多有一個主元索引。
    """