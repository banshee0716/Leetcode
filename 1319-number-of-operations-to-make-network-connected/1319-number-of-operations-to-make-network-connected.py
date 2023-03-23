import collections
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n-1: # this is a edge condi. to connect n components we need min n-1 cables. 
            return -1
        
        
        d=collections.defaultdict(list) # converting given list to adjacency list as it will help us to run dfs function.
        for i ,j in connections:
            d[i].append(j)
            d[j].append(i)
        
        
        visited=set()    # this will track the visited vertex
        numofconnected=0 # this will track the no. of separate  components
        
        
        def dfs(root):
            visited.add(root)
            for j in d[root]:# traversing each neighbour vertex of root and visit them in one go and add them to visited
                if j not in visited:
                    dfs(j)
        
        
        for i in range(n): # running loop to track how many vertex we can visit through i 
            if i not in visited:
                numofconnected+=1# as this is not visited so this will be the start of a new separate component .
                dfs(i)
        return numofconnected-1 # to connect n separate components we require min n-1 cables .
        