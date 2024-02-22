class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        """
        REQUIREMENTS:
        1. Input = List (array)
        2. RETURN = int
        Complexity
        Time = O(nlogn)
        DATA STRUCTURE = arrays
        ALGORITHM = Two pointers
        PSEUDOCODE:
        1. Declare an array called sortedArray
        2. Append the sorted version of our skill
        3. Declare variables sum_, count = sortedArray[0] + sortedArray[len(sortedArray) - 1], sortedArray[0] * sortedArray[len(sortedArray) - 1]
        4. Declare left = 1
        5. Declare right = len(sortedArray) - 2
        6. Iterate until left <= right
        7.   If sortedArray[left] + sortedArray[right] != sum_:
        8.     Return -1
        9.   Else:
        10.    Increment count by sortedArray[left] * sortedArray[right]
        11.    Increment left
        12.    Decrement right
        13. Return count
        """
        if len(skill) % 2 != 0:
            return -1
        else:
            sortedArray = sorted(skill)
            sum_ = sortedArray[0] + sortedArray[len(sortedArray) - 1]
            count = sortedArray[0] * sortedArray[len(sortedArray) - 1]
            left = 1
            right = len(sortedArray) - 2
            while left <= right:
                if sortedArray[left] + sortedArray[right] != sum_:
                    return -1
                else:
                    count += sortedArray[left] * sortedArray[right]
                left += 1
                right -= 1
            return count
