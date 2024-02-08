class Solution:
    def numSquares(self, n: int) -> int:
        # 創建小於等於n的所有完全平方數列表
        squares = [i**2 for i in range(1, int(n**0.5) + 1)]
        d, q, nq = 1, {n}, set()
        
        while q:
            for node in q:
                for square in squares:
                    if node == square:  # 直接找到答案
                        return d
                    if node < square:  # 無需繼續遍歷更大的完全平方數
                        break
                    nq.add(node - square)
            q, nq, d = nq, set(), d + 1  # 更新變數，準備下一輪搜索

    
    """
    
解題思路
這道題目可以透過廣度優先搜索（Breadth-First Search, BFS）來解決。首先，創建一個列表squares，裡面包含了所有小於等於n的完全平方數。然後，使用BFS來尋找最短路徑，即最少步驟到達n。

創建完全平方數列表：
利用列表解析式創建一個包含所有小於等於n的完全平方數的列表squares。

初始化變數：
d為深度（或步數），從1開始。
q為當前層次的節點集合，初始只包含n。
nq為下一層次的節點集合，初始化為空集合。

BFS搜索：
當q非空時，對於q中的每個節點node，遍歷squares列表。
如果node等於某個完全平方數，則找到了答案，返回d。
如果node小於某個完全平方數，則無需繼續遍歷更大的完全平方數。
否則，將node-square加入到nq中。
搜索結束後，更新q為nq，nq清空，並將d增加1。
    
時間複雜度
    -創建完全平方數列表的時間複雜度為O(√n)。
    -BFS的最壞情況時間複雜度為O(n)，因為每一次減去一個完全平方數可能遍歷整個squares列表。
    -總的時間複雜度為O(n√n)，因為每層BFS可能需要遍歷所有小於n的完全平方數。

空間複雜度
    -squares列表的空間複雜度為O(√n)。
    -BFS過程中，集合q和nq的空間複雜度最壞情況下為O(n)。
    -總的空間複雜度為O(n)。
    """