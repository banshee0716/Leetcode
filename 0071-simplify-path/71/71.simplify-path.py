#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        # 將路徑用 "/" 分割為元素
        arr = path.split("/")
        new_path = []
        # 遍歷元素陣列
        for index, ele in enumerate(arr):
            if ele == "." or ele == "":  # "." 表示當前目錄，跳過
                continue
            elif ele == "..":  # ".." 表示上一級目錄，刪除新陣列中的最後一個元素
                if new_path:
                    new_path.pop()
            else:
                new_path.append(ele)  # 正常目錄元素加入新陣列中
        # 拼接新路徑，頭部加上 "/"
        return "/" + "/".join(new_path)


"""
這是一個將給定的路徑字串化簡的問題，例如 "/a//b////c/d//././/.." 經過化簡後變為 "/a/b/c"，其
中單個 "." 表示當前目錄，".." 表示上一級目錄，"//" 表示多餘的斜線。
"""

"""
時間複雜度：
遍歷一次元素陣列需要 O(n) 時間，其中 n 為元素個數，而每次刪除新陣列中的最後一個元素需要 O(1) 時間，因此整個算法的時間複雜度為 O(n)。

空間複雜度：
使用了一個新陣列存儲簡化後的路徑，其最大長度為 n，因此空間複雜度為 O(n)。
"""
# @lc code=end
