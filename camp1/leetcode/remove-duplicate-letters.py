
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        counter =  Counter(s)
        Stackcount = defaultdict(int)
        for i in range(len(s)):
            while stack and stack[-1] > s[i] and counter[stack[-1]] >1 and Stackcount[s[i]] <1:
                val = stack.pop()
                counter[val] -= 1
                Stackcount[val] -=1
            if Stackcount[s[i]] <1:
                stack.append(s[i])
                Stackcount[s[i]] +=1
            else:
                counter[s[i]] -=1
        return ''.join(stack)
