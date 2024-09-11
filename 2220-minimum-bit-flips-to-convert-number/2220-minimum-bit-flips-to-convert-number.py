class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return (start ^ goal).bit_count()
        
        
        
    """
數字 x 的位元翻轉是在 x 的二進位表示中選擇一個位元並將其從 0 翻轉到 1 或從 1 翻轉到 0。

例如，對於 x = 7，二進位表示為 111，我們可以選擇任何位元（包括未顯示的任何前導零）並將其翻轉。我們可以翻轉右側第一位得到 110，翻轉右側第二位得到 101，翻轉右側第五位（前導零）得到 10111，等等。
給定兩個整數 start 和 goal，傳回將 start 轉換為 goal 的最小位元翻轉次數。
    """