from typing import List

class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        # 將每個技能映射到一個位元
        bit_skills = {skill: 1 << i for i, skill in enumerate(req_skills)}

        # 計算目標技能的位元表示
        target_skills = (1 << len(req_skills)) - 1

        # 初始化動態規劃表
        dp = [None] * (target_skills + 1)
        dp[0] = []

        # 遍歷每個人，更新動態規劃表
        for i, person_skills in enumerate(people):
            # 計算此人的技能位元掩碼
            person_bitmask = sum(bit_skills[skill] for skill in person_skills if skill in bit_skills)
            for covered_skills, team in enumerate(dp):
                if team is None:
                    continue
                new_skills = covered_skills | person_bitmask
                if new_skills == covered_skills:
                    continue
                # 如果 dp[new_skills] 為 None 或新的團隊比舊的團隊人數少
                if dp[new_skills] is None or len(dp[new_skills]) > len(team) + 1:
                    dp[new_skills] = team + [i]

        return dp[target_skills]

    
"""
1. 將每個技能映射到一個位元，這是通過位元掩碼來完成的。我們創建了一個bit_skills的字典，將每個技能映射到一個單獨的位元上。
2. 計算目標技能，這就是我們所需要的所有技能的位元表示。對於n個技能，其位元表示就是1 << n - 1。
3. 創建一個動態規劃的表，表的大小是目標技能的位元表示加1，初始化所有的元素為None，除了第一個元素為空陣列。
4. 對於每個人，我們計算他們的技能位元掩碼，並在動態規劃表中更新相對應的最小團隊大小。
5. 最後，返回與目標技能相對應的最小團隊大小。


時間複雜度是O(N * 2^S)，其中N是人數，S是技能數。在最壞的情況下，我們可能需要遍歷每一個人對每一種技能組合的情況。所以時間複雜度是O(N * 2^S)。

空間複雜度是O(2^S)，我們需要一個大小為2^S的數組來存儲動態規劃的狀態。
"""