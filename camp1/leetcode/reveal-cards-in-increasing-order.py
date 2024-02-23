class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        ans = [0]*len(deck)
        queue = deque()
        for i in range(len(deck)):
            queue.append(i)
        i = 0
        while queue and i < len(deck):
            val = queue.popleft()
            ans[val] = deck[i]
            if queue:
                num = queue.popleft()
                queue.append(num)
            i += 1
        return ans