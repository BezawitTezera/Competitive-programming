class Solution:
    def smallestNumber(self, num: int) -> int:
        if num < 10 and num >= 0:
            return num
        val = str(num)
        ans = list(val)
        if num < 0:
            ans.remove('-')
            ans.sort(reverse = True)
            return int('-' + ''.join(ans))
        else:
            ans.sort()
            Count = ans.count('0')
            if Count >= 1:
                ans[Count], ans[0] = ans[0], ans[Count]
            return int(''.join(ans))
        