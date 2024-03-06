class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        index = bisect_right(letters, target)
        
        if index < len(letters):
            return letters[index]
        else:
            return letters[0]

