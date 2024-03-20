class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        counter = defaultdict(int)
        min_ = float('inf')

        for i in range(k):
            counter[blocks[i]] += 1
        
        if k == len(blocks):
            return counter['W']
        
        for i in range(k, len(blocks)):
            min_ = min(min_, counter['W'])
            counter[blocks[i - k]] -= 1
            counter[blocks[i]] += 1

        min_ = min(min_, counter['W'])
        return min_ 
       
        