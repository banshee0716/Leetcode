class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        # 初始化行數（res）為1和當前行使用的寬度（cur）為0
        res, cur = 1, 0
        
        # 遍歷字串中的每個字元
        for i in s:
            # 獲取該字元的寬度
            width = widths[ord(i) - ord('a')]
            
            # 判斷該字元是否需要換行
            if cur + width > 100:
                # 換行，行數增加1，並將當前行的寬度設置為該字元的寬度
                res += 1
                cur = width
            else:
                # 不換行，將該字元的寬度加到當前行的寬度上
                cur += width
                
        # 返回行數和最後一行使用的寬度
        return [res, cur]
"""
時間複雜度為O(n)，其中n是字串的長度。
關於空間複雜度，由於我們只使用了常數級別的額外空間，因此空間複雜度為O(1)。

"""