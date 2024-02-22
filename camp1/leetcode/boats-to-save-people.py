class Solution:
    @staticmethod
    def numRescueBoats(people, limit):
        """
        REQUIREMENT:
        INPUT = People (array), Limit (int)
        RETURN = int
        DATA STRUCTURE = array
        ALGORITHM = Two pointer
        TIME COMPLEXITY = O(n)
        SPACE COMPLEXITY = O(n)
        PSEUDOCODE:
        1. Create sortedArray = sorted(people)
        2. Declare i = 0
        3. Declare j = len(people) - 1
        4. Declare a variable, count = 0
        5. Iterate until i <= j
        6.   If people[i] + people[j] <= limit:
        7.     Increment count by 1
        8.     Increment i
        9.     Decrement j
        10.  Else:
        11.    Increment count by 1
        12.    Decrement j
        13.  Return count
        """
        people.sort()
        i = 0
        j = len(people) - 1
        count = 0
        while i <= j:
            if people[i] + people[j] <= limit:
                count += 1
                i += 1
                j -= 1
            else:
                count += 1
                j -= 1
        return count