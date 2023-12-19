from typing import List

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row, col = len(img), len(img[0])  # 圖片的行列數
        result = [[0] * col for _ in range(row)]  # 初始化結果矩陣

        # 遍歷每個單元
        for i in range(row):
            for j in range(col):
                total_sum = 0  # 周圍單元的灰度總和
                count = 0  # 周圍單元的數量

                # 計算周圍單元的灰度平均值
                for x in range(max(0, i - 1), min(row, i + 2)):
                    for y in range(max(0, j - 1), min(col, j + 2)):
                        total_sum += img[x][y]
                        count += 1

                result[i][j] = total_sum // count  # 設置平均灰度值

        return result

# 使用black格式化後的代碼與上述代碼在格式上已經符合標準


        
"""
影像平滑器是大小為3 x 3 的濾波器，可以透過向下舍入單元格和周圍八個單元格的平均值（即藍色平滑器中九個單元格的平均值）來應用於影像的每個單元格。如果某個單元格的一個或多個周圍單元格不存在，我們不會將其視為平均值（即紅色平滑器中四個單元格的平均值）。

給定一個代表影像灰階的 m x n 整數矩陣 img，在對影像的每個單元套用平滑器後傳回影像。


解題思路：

1. 初始化結果矩陣：
    -創建一個新的二維矩陣 result，其尺寸與輸入的圖片 img 相同。

2.遍歷圖片的每個像素：
    -對於圖片中的每個像素，計算它及其周圍像素的總和和像素個數。

3.計算周圍像素的平均值：
    -對於每個像素，找出它周圍（包括自己）所有可達的像素，計算這些像素的總和及數量，然後求出平均值。

4. 更新結果矩陣：
    -將計算出的平均值放入 result 矩陣對應的位置。
    
時間複雜度分析：

    -遍歷整個圖片的時間複雜度為 O(row * col)，其中 row 和 col 分別是圖片的行數和列數。
    -對於圖片中的每個像素，需要遍歷其周圍最多9個像素，這部分的時間複雜度為 O(1)。
    -因此，總的時間複雜度為 O(row * col)。

空間複雜度分析：
    -需要額外的空間來存儲結果矩陣 result，其空間複雜度為 O(row * col)。
"""