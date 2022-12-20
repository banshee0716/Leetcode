class Solution:
    def canVisitAllRooms(self, rooms):
        visited = set([0])
        
        def dfs(room):
            for neib in rooms[room]:
                if neib not in visited:
                    visited.add(neib)
                    dfs(neib)
                    
        dfs(0)
        return len(visited) == len(rooms)    
    
    # Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, 
    # return true if you can visit all the rooms, or false otherwise.