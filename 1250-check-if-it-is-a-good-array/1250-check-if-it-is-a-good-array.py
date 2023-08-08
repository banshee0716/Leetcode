class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        # 初始化 gcd 為 nums 的第一個元素
        gcd = nums[0]
        
        # 遍歷 nums 中的每一個數
        for i in nums:
            # 使用歐幾里得算法找到 gcd 和 i 的最大公約數
            while i:
                gcd, i = i, gcd % i
                
        # 如果最後計算出來的最大公約數是 1，則返回 True，否則返回 False
        return gcd == 1

        
"""
基於 Bézout 的引理，該引理指出：對於任意的整數 a 和 b，若 d 是 a 和 b 的最大公約數 (GCD)，則必定存在整數 x 和 y 使得 ax + by = d。
對於這道題，我們要確定是否存在某些數字的線性組合得到 1，這意味著我們需要判斷數組中所有數字的 GCD 是否為 1。

時間複雜度: O(n*logC) 其中 n 是 nums 的長度，C 是 nums 中數字的最大值。我們遍歷了 nums 的每一個數字且每次都使用歐幾里得算法計算最大公約數，歐幾里得算法的時間複雜度是 O(logC)。

空間複雜度: O(1) 我們只使用了有限的額外空間。
"""