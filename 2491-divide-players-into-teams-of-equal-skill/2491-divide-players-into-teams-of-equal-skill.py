class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # 如果只有兩個玩家，則直接返回他們的技能值乘積
        if len(skill) == 2:
            return skill[0] * skill[1]
        
        # 將玩家的技能值進行排序
        skill.sort()
        
        ans, sum_ = 0, 0
        ptr1, ptr2 = 0, len(skill) - 1
        
        for i in range(len(skill) // 2):
            # 如果是第一組，則計算技能值總和，並將技能值乘積累加到總分
            if i == 0:
                sum_ = skill[ptr1] + skill[ptr2]
                ans +=  (skill[ptr1] * skill[ptr2])
            else:
                # 如果這一組的技能值總和不等於上一組的技能值總和，則返回-1
                if skill[ptr1] + skill[ptr2] != sum_:
                    return -1
                
                # 將技能值乘積累加到總分
                ans += (skill[ptr1] * skill[ptr2])
            
            # 將頭尾指針向中間移動
            ptr1 += 1
            ptr2 -= 1
            
        return ans # 返回總分

"""
兩兩一組能力要一樣，最大的跟最小的放一起，以此類推到中間。用雙指針處理，如果發現相加不同代表沒救了返回-1，還對的話就繼續累加

時間複雜度為 O(n log n)，其中 n 是 skill 陣列的長度。這是因為我們需要對技能值進行排序，排序的時間複雜度為 O(n log n)。
空間複雜度為 O(1)，因為我們只使用了常數空間來存儲變數。
"""