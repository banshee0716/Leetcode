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