class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        """
        REQUIREMENTS:
        1. INPUT = list
        2. RETURN = int
        Time complexity: O(n)
        PSUEDOCODE:
        1. Sort the piles 
        2. choose two numbers from the end one from the start
        3. append them to a new array ans
        4. pop the chosen elements
        5. iterate until len(piles) is less than 3
        """
        piles.sort()
        count = 0
        print(piles)  
        while len(piles) >= 3:
            ans = []
            ans.append(piles.pop())
            ans.append(piles.pop())
            ans.append(piles.pop(0))
            count += ans[1]
        return count
