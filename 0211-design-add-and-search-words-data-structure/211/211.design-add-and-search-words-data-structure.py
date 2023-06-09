#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start
class TrieNode:
    def __init__(self):
        self.children = {}  # 用來儲存子節點的字典
        self.end_node = 0  # 結束節點標記


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()  # 初始化字典樹的根節點

    def addWord(self, word):
        root = self.root
        for symbol in word:
            root = root.children.setdefault(symbol, TrieNode())  # 逐個字符建立節點
        root.end_node = 1  # 標記結束節點

    def search(self, word):
        def dfs(node, i):
            if i == len(word):
                return node.end_node  # 如果到達字串末尾，返回結束節點標記

            if word[i] == ".":
                for child in node.children:  # 對於所有的子節點
                    if dfs(node.children[child], i + 1):
                        return True  # 遞迴搜索子樹，如果找到就返回True

            if word[i] in node.children:
                return dfs(node.children[word[i]], i + 1)  # 按照字串索引遞迴搜索

            return False  # 字符不匹配，直接返回False

        return dfs(self.root, 0)  # 從根節點開始搜索


"""
時間複雜度分析：

addWord：對於每個單詞，需要遍歷每個字符，因此時間複雜度為O(k)，其中k為單詞的長度。插入n個單詞的時間複雜度為O(nk)。
search：最壞情況下需要遍歷整個字典樹，時間複雜度為O(nk)，其中n為字典中單詞的數量。

空間複雜度分析：

addWord：對於每個單詞，需要建立一個新的節點，因此空間複雜度為O(nk)，其中n為單詞的數量，k為最長的單詞長度。
search：搜索過程中需要遞迴調用，因此空間複雜度與字典樹的高度有關，最壞情況下為O(k)。
"""

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end
