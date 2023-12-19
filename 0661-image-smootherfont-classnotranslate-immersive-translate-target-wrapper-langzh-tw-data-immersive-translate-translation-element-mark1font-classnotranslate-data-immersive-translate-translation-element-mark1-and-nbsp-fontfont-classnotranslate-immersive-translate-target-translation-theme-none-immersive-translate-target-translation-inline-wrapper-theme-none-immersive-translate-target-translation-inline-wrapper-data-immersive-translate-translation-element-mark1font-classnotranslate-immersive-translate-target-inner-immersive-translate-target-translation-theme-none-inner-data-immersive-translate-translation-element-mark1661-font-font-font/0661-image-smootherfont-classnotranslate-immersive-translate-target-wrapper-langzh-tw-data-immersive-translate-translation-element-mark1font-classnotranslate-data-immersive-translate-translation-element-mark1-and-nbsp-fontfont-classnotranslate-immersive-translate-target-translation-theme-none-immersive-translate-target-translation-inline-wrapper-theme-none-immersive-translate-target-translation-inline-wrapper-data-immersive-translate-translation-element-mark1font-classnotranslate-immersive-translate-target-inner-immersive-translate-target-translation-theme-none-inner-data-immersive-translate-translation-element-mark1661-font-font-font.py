class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row, col = len(img), len(img[0])
        result = [[0] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                total_sum = 0
                count = 0
                for x in range(max(0, i-1), min(row, i+2)):
                    for y in range(max(0, j-1), min(col, j+2)):
                        
                        total_sum += img[x][y]
                        count += 1
                
                result[i][j] = total_sum // count
                
        return result
        
        

        
"""
影像平滑器是大小為3 x 3 的濾波器，可以透過向下舍入單元格和周圍八個單元格的平均值（即藍色平滑器中九個單元格的平均值）來應用於影像的每個單元格。如果某個單元格的一個或多個周圍單元格不存在，我們不會將其視為平均值（即紅色平滑器中四個單元格的平均值）。

給定一個代表影像灰階的 m x n 整數矩陣 img，在對影像的每個單元套用平滑器後傳回影像。
"""