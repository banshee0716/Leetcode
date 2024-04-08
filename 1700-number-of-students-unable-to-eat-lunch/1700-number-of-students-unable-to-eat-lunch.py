from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = [0, 0]  # count[0] 為喜歡圓形三明治的學生數，count[1] 為喜歡方形三明治的學生數
        
        # 計數喜歡不同三明治的學生數量
        for student in students:
            count[student] += 1
        
        # 遍歷每種三明治
        for sandwich in sandwiches:
            if count[sandwich] == 0:  # 如果沒有學生喜歡當前這種三明治，結束遍歷
                break
            count[sandwich] -= 1  # 有學生拿走一份三明治，相應計數減一
        
        # 返回無法吃午餐的學生數量（即剩下的學生總數）
        return count[0] + count[1]

        
    """
我們可以嘗試不直接模擬學生排隊的過程，而是通過計數不同偏好的學生數量來實現。
由於只有兩種類型的三明治和兩種類型的學生偏好，我們可以用兩個變量來追蹤喜歡圓形三明治（假設為0）和方形三明治（假設為1）的學生數量。
然後，對於每種類型的三明治，如果有學生喜歡它，我們就減少相應的計數，直到某種三明治沒有學生喜歡為止。    
    
時間複雜度分析
計算喜歡不同三明治的學生數量的時間複雜度為O(N)，其中N是學生數量。
遍歷三明治的時間複雜度為O(M)，其中M是三明治的數量。
因此，總時間複雜度為O(N + M)。

空間複雜度分析
額外使用了一個固定大小的數組來存儲兩種偏好的學生數量，因此空間複雜度為O(1)。
    """