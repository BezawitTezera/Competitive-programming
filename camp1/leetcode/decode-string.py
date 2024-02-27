class Solution:
    def decodeString(self, s: str) -> str:
        def decode(left, right):
            ans = ""
            digit = ""
            num = 0
            count = 0
            start = -1
            for i in range(left, right):
                if s[i].isdigit():
                    digit += s[i]
                elif s[i] == '[':
                    if count == 0:
                        num = int(digit)
                        start = i
                    count += 1
                    digit = ""
                elif s[i] == ']':
                    count -= 1
                    if count == 0:
                        ans += num* decode(start + 1, i)      
                elif count == 0:
                    ans += s[i]
            return ans
        return decode(0, len(s))