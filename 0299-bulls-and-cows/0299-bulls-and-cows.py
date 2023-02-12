class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull, cow = 0, 0
        s = [0] * 10
        g = [0] * 10
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
            else:
                s[int(secret[i])] += 1
                g[int(guess[i])] += 1
        for i in range(10):
            cow += min(s[i], g[i])
        return str(bull) + "A" + str(cow) + "B"
