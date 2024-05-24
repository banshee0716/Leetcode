class Solution:
    def maxScoreWords(
        self, words: List[str], letters: List[str], score: List[int]
    ) -> int:
        lettersCounter = Counter(letters)
        totalScore = 0

        def explore(index, letterCounter, currScore):
            nonlocal totalScore

            totalScore = max(totalScore, currScore)
            if index == len(words):
                return

            for i in range(index, len(words)):
                tmpCounter = copy.deepcopy(letterCounter)
                word = words[i]
                wordScore = 0
                isValid = True

                for ch in word:
                    if ch in tmpCounter and tmpCounter[ch] > 0:
                        tmpCounter[ch] -= 1
                        wordScore += score[ord(ch) - ord("a")]
                    else:
                        isValid = False
                        break
                if isValid:
                    explore(i + 1, tmpCounter, currScore + wordScore)

        explore(0, lettersCounter, 0)
        return totalScore
        
        
    
    
    """
給定單字清單、單個字母列表（可能重複）以及每個字元的分數。

傳回使用給定字母形成的任何有效單字集的最高分（單字 [i] 不能使用兩次或多次）。

不必使用字母中的所有字符，每個字母只能使用一次。字母「a」、「b」、「c」、...、「z」的分數分別由 Score[0]、score[1]、...、score[25] 給出。
    """