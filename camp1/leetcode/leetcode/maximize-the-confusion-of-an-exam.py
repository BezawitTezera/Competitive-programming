class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        max_ = 0
        Scount = defaultdict(int)
        count = 0
        i = 0

        for j in range(len(answerKey)):
            Scount[answerKey[j]] += 1
            count = max(count, Scount[answerKey[j]])

            while j - i + 1- count > k:
                Scount[answerKey[i]] -= 1
                i += 1
            
            max_ = max(max_, j - i + 1)
        return max_
