class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        # 初始化兩個變數x和y用於保存nums1和nums2中元素的XOR結果
        x, y = 0, 0
        
        # 計算nums1中所有元素的XOR結果
        for a in nums1:
            x ^= a
        
        # 計算nums2中所有元素的XOR結果
        for b in nums2:
            y ^= b
        
        # 使用XOR屬性：
        # 如果len(nums1)是奇數，y的XOR結果會影響到最終結果。
        # 如果len(nums2)是奇數，x的XOR結果會影響到最終結果。
        return (len(nums1) % 2 * y) ^ (len(nums2) % 2 * x)

        
"""
要求從兩個陣列中計算出一個第三個陣列nums3，這個陣列包含了nums1和nums2中所有元素配對的位元XOR結果。然後要返回這個新陣列中所有元素的XOR結果。

解題思路：

由於XOR操作具有交換性和結合性，所以我們可以先分別計算nums1和nums2中所有元素的XOR結果。
利用XOR的屬性，如果nums1的長度是奇數，則nums2中所有元素的XOR結果會影響到最終結果；反之亦然。

時間複雜度：O(m+n)，其中m和n分別是nums1和nums2的長度。
空間複雜度：O(1)，因為我們只使用了常數的額外空間。
"""