class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        n = len(bills)
        five = ten = 0
        for i in range(n):
            if bills[i] == 5:
                five += 1
            elif bills[i] == 10:
                five -= 1
                ten += 1
            elif ten > 0:
                ten -= 1
                five -= 1
            else:
                five -= 3
            if five < 0:
                return False
        return True