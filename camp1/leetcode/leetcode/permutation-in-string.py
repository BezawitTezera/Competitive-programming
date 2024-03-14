class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return 
            
        s1count = Counter(s1)
        k = len(s1)
        Scount = Counter(s2[:k])

        for i in range(k, len(s2)):
            if s1count == Scount:
                return True

            Scount[s2[i]] += 1
            Scount[s2[i - k]] -= 1
            if Scount[s2[i - k]] == 0:
                del Scount[s2[i - k]]

        return s1count == Scount