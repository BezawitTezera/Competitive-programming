class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        ans = []
        path = ""
        phoneNumber = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

        def backtrack(path, next):
            if len(next) == 0:
                return ans.append(path)

            for letter in phoneNumber[next[0]]:
                backtrack(path + letter, next[1:])

        backtrack(path, digits)
        return ans

            