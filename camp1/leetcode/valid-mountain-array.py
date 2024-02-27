class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) <= 2:
            return False
        else:
            i = 0
            j = len(arr) - 1
            while i < j:
                if i == len(arr) - 1 or j == 0:
                    return False
                else: 
                    if arr[i] < arr[i + 1]:
                        i += 1
                    elif arr[j] < arr[j - 1]:
                        j -= 1
                    else:
                        break
            if i == 0 or j == len(arr) - 1:
                return False
            else:
                return i == j
