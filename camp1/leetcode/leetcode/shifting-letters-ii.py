class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        store = [0] * (len(s) + 1)
        string = []

        for letter in s:
            string.append(ord(letter) - 97)
            

        for i in range(len(shifts)):
            if shifts[i][2] == 0:
                store[shifts[i][0]] -= 1
                store[shifts[i][1] + 1] += 1
            else:
                store[shifts[i][0]] += 1
                store[shifts[i][1] + 1] -= 1
        
        sum_ = 0
        for i in range(len(store)):
            sum_ += store[i]
            store[i] = sum_
        store.pop()

        ans = ""
        for i in range(len(string)):
            string[i] += store[i]
            ans += chr((string[i]) % 26 + 97)

        return ans

        
