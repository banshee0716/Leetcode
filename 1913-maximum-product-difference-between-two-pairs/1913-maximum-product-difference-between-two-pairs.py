from typing import List

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        biggest = 0  # 最大值
        second_biggest = 0  # 次大值
        smallest = float('inf')  # 最小值
        second_smallest = float('inf')  # 次小值

        # 遍歷數組更新這四個變量
        for num in nums:
            if num > biggest:
                second_biggest, biggest = biggest, num
            elif num > second_biggest:
                second_biggest = num
            
            if num < smallest:
                second_smallest, smallest = smallest, num
            elif num < second_smallest:
                second_smallest = num

        # 計算最大乘積差
        return biggest * second_biggest - smallest * second_smallest

"""
解題思路：

尋找最大和次大元素：
    -初始化兩個變量 biggest 和 second_biggest 來存儲數組中的最大和次大元素。初始值設為0。

尋找最小和次小元素：
    -初始化兩個變量 smallest 和 second_smallest 來存儲數組中的最小和次小元素。初始值設為無窮大。

遍歷數組：
    -遍歷數組，更新這四個變量的值。

計算最大乘積差：
    -計算最大值和次大值的乘積以及最小值和次小值的乘積，然後求它們的差
    
時間複雜度分析：
遍歷數組的時間複雜度為 O(n)，其中 n 是數組的長度。

空間複雜度分析：
這個算法只使用了固定數量的額外空間來存儲變量，因此空間複雜度為 O(1)。

"""