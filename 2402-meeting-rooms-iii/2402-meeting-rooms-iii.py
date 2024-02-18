import heapq
from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()  # 根據會議的開始時間進行排序
        free_rooms = list(range(n))  # 所有的空閒會議室
        busy_rooms = []  # 當前被佔用的會議室
        count = [0] * n  # 每個會議室被預定的次數
        
        for start, end in meetings:
            # 釋放已經結束的會議室
            while busy_rooms and busy_rooms[0][0] <= start:
                _, room = heapq.heappop(busy_rooms)
                heapq.heappush(free_rooms, room)
            
            # 分配會議室
            if free_rooms:
                room = heapq.heappop(free_rooms)
            else:
                end_time, room = heapq.heappop(busy_rooms)
                end += end_time - start
            
            # 預定會議室
            heapq.heappush(busy_rooms, (end, room))
            count[room] += 1
        
        # 找到預定次數最多的會議室
        max_booked = max(count)
        for i in range(n):
            if count[i] == max_booked:
                return i
    
    
    """
解題思路
1. 排序會議：
    -首先，根據會議的開始時間對會議進行排序，以確保我們按時間順序處理它們。

2. 初始化數據結構：
    -使用一個最小堆free_rooms來跟蹤所有空閒的會議室，並將它們的索引加入到堆中。
    -使用另一個最小堆busy_rooms來管理當前被佔用的會議室，其中元素是一個元組(會議結束時間, 會議室索引)。
    -使用一個數組count來記錄每個會議室被預定的次數。

3. 遍歷會議：
    -對於每個會議，先檢查是否有會議室已經空閒（即busy_rooms中有會議已經結束）。如果有，則將其從busy_rooms移動到free_rooms。
    -如果有空閒的會議室（free_rooms非空），則從中取出一個會議室並分配給當前會議。
    -如果沒有空閒的會議室，則從busy_rooms中取出最早釋放的會議室，並將當前會議延後至該會議室釋放。
    -更新會議室的佔用情況，並增加該會議室的預定次數。

4. 找出預定次數最多的會議室：
    -遍歷count數組，找到預定次數最多的會議室，返回其索引。

時間複雜度
    -排序會議的時間複雜度為O(MlogM)，其中M是會議的數量。
    -遍歷會議並處理每個會議的時間複雜度為O(MlogN)，其中N是會議室的數量。
    -總體時間複雜度為O(MlogM + MlogN)。

空間複雜度
    -使用了額外的空間來存儲空閒和佔用的會議室堆，以及預定次數的數組，空間複雜度為O(N)。
    """
    
    