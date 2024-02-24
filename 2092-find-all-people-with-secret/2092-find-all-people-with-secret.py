class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        known_set = set([0, firstPerson])
        
        sorted_meetings = []
        meetings.sort(key=lambda x:x[2])

        seen_time = set()
        
        for meeting in meetings:
            if meeting[2] not in seen_time:
                seen_time.add(meeting[2])
                sorted_meetings.append([])
            sorted_meetings[-1].append((meeting[0], meeting[1]))

        for meeting_group in sorted_meetings:
            people_know_secret = set()
            graph = defaultdict(list)
            
            for p1, p2 in meeting_group:
                graph[p1].append(p2)
                graph[p2].append(p1)
                if p1 in known_set:
                    people_know_secret.add(p1)
                if p2 in known_set:
                    people_know_secret.add(p2)
                    
            queue = deque((people_know_secret))
        
            while queue:
                curr = queue.popleft()
                known_set.add(curr)
                for neighbor in graph[curr]:
                    if neighbor not in known_set:
                        known_set.add(neighbor)
                        queue.append(neighbor)

        return list(known_set)
    
"""
「找出知道秘密的所有專家」要求在給定一系列會議和首位知道秘密的人後，找出最終知道秘密的所有人的列表。

解題思路

初始化已知秘密的人員集合：
    -首先，將0（發起人）和firstPerson加入到已知秘密的人員集合known_set中。

對會議按時間排序並分組：
    -根據會議的時間將會議排序，並將同一時間的會議分組放入sorted_meetings中，以便按時間順序處理會議。

建立每組會議的圖並傳播秘密：
    -對於每一組會議，建立一個圖graph，圖中的節點表示參會者，邊表示他們之間的會面。
    -遍歷這組會議，將已知秘密的人加入people_know_secret集合。
    -使用廣度優先搜索（BFS）從people_know_secret中的每個人開始，傳播秘密給所有可達的人，即更新known_set。

返回結果：
    -將known_set轉換成列表形式返回，表示最終知道秘密的所有人。
    
時間複雜度
    -對會議進行排序的時間複雜度為O(MlogM)，其中M是會議的數量。
    -建立圖和進行BFS的時間複雜度為O(M+N)，其中N是參會人數。
    -總的時間複雜度為O(MlogM + M + N)。

空間複雜度
    -需要額外的空間來存儲排序後的會議sorted_meetings、圖graph和BFS的隊列queue。
    -空間複雜度為O(M + N)。
"""