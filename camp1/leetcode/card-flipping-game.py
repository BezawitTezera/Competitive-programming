class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        badInt = set()
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                badInt.add(fronts[i])
        min_ = float("inf")
        for i in (fronts + backs):
            if i not in badInt:
                min_ = min(min_, i)
        return min_ if min_ != float("inf") else 0
