class Solution:
    def sortSentence(self, s: str) -> str:       
        s = s.split()
        ans = [0] * len(s)
        for sentence in s:
            val = int(sentence[-1])
            ans[val-1]=sentence[:len(sentence)-1]
        return ' '.join(ans)