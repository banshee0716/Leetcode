class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boat, low, high = 0, 0, len(people) - 1
        # 將人按體重排序
        people.sort()
        while low <= high:
            # 如果最重的人和最輕的人的體重和小於等於限制，那麼兩個人可以坐在同一艘船上
            if people[low] + people[high] <= limit:
                low += 1
            
            # 如果最重的人和最輕的人的體重和大於限制，那麼最重的人只能坐在一艘船上
            boat += 1
            high -= 1
            
        return boat
        
        
    """
給你一個陣列 people，其中 people[i] 是第 i 個人的重量，以及無限數量的船，其中每艘船可以承載的最大重量為 limit。
每艘船最多同時載運兩人，前提是這些人的重量總和不得超過限制。

返回承載每個指定人員的最少船隻數量。
    """