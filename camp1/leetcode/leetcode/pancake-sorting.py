class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        k = []
        for i in range(n):
            max_ = max(arr[:n-i])
            index = arr.index(max_) + 1
            arr[:index] = arr[:index][::-1]
            k.append(index)
            arr[:n-i] = arr[:n-i][::-1]
            k.append(n-i)
        return k
