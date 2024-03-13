class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        Scount = defaultdict(int)
        Pcount = Counter(p)
        k = len(p)

        for i in range(k):
            Scount[s[i]] += 1
        ans = []

        for i in range(k, len(s)):
            if Pcount == Scount:
                ans.append(i-k)

            Scount[s[i - k]] -= 1
            if Scount[s[i - k]] == 0:
                del Scount[s[i - k]]

            Scount[s[i]] += 1
            
        if Pcount == Scount:
            ans.append(len(s)-k)
        
        return ans
