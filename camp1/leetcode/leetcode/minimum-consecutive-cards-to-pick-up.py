class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        visited = set()
        min_ = float('inf')
        sum_ = 0
        i = 0
        for j in range(len(cards)):
            while cards[j] in visited:
                sum_ = len(visited)  + 1
                min_ = min(min_ , sum_)
                visited.remove(cards[i])
                i += 1
            
            visited.add(cards[j])
        
        if len(cards) == len(visited):
            return -1
            
        return min_
