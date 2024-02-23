class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        """
        REQUIREMENT:
        1. INPUT: n (int, [1:n+1]) and k, the number of swaps
        2. RETURN: last element
        PSEUDOCODE:
        1. ans an empty list
        2. append values uptp n
        3.iterate through every element and pop every kth element
        4. return ans
        """
        ans = list(range(1, n + 1))
        i = 0
        while len(ans) > 1:
            i = (i + k - 1)% len(ans)
            ans.pop(i)
        return ans[0]
   