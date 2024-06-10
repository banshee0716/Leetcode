class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(h1 != h2 for h1, h2 in zip(heights, sorted(heights)))
        
        
        
        
        
    """
一所學校正試圖為所有學生拍攝一張年度照片。請學生依身高非遞減順序排成一列。讓這個排序由預期的整數數組表示，其中預期[i]是隊列中第 i 個學生的預期身高。
給定一個整數數組 height ，表示學生目前站立的順序。
傳回高度[i] !=預期[i]的索引數。
    """