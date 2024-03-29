class Solution:
    def __init__(self):
        self.scrambles = {}
        
    def isScramble(self, s1: str, s2: str) -> bool:
        if (s1, s2) in self.scrambles:
            return self.scrambles[(s1, s2)]
        if s1 == s2:
            self.scrambles[(s1, s2)] = True
            return True
        ls = len(s1)
        if ls == 1 or sorted(s1) != sorted(s2):
            self.scrambles[(s1, s2)] = False
            return False

        for i in range(1, ls):
            
            s1_left, s1_right = s1[:i], s1[i:]
            s2_left, s2_right = s2[:i], s2[i:]
            match1 = self.isScramble(s1_left, s2_left) and self.isScramble(s1_right, s2_right)
            
            s2_left2, s2_right2 = s2[:ls - i], s2[ls - i:]
            match2 = self.isScramble(s1_left, s2_right2) and self.isScramble(s1_right, s2_left2)
            
            if match1 or match2:
                self.scrambles[(s1, s2)] = True
                return True
            
        self.scrambles[(s1, s2)] = False
        return False