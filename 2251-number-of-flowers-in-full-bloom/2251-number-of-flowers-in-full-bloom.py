class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        
        start = sorted([s for s, e in flowers])
        end = sorted([e for s, e in flowers])
        return [bisect_right(start, t) - bisect_left(end, t) for t in people]
        
    """
給定一個 0 索引的 2D 整數陣列 Flowers，其中 Flowers[i] = [starti, endi] 表示第 i 朵花將從 starti 到 endi（含）盛開。
您還會獲得一個大小為 n 的 0 索引整數數組 people，其中 people[i] 是第 i 個人到達看花的時間。

傳回大小為 n 的整數數組answer，其中answer[i]是第i個人到達時盛開的花朵的數量。
    """