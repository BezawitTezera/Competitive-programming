class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        """
        1. create an empty array for elements in arr1 only and another for the elements in arr2
        2. append the values not in arr2
        3. i iterates through all elements in arr2
        4. nums elements in arr2
        if num in arr[i] == num, then append in sortedarray
        5. extend the two arrays and return
        """
        unsorted = []
        sortedVal = []
        for num in arr1:
            if num not in arr2:
                unsorted.append(num)
        unsorted.sort()
        print(unsorted)
        for i in range(len(arr2)):
            for num in arr1:
                if arr2[i] == num:
                    sortedVal.append(num)
                    print(sortedVal)
        sortedVal = sortedVal + unsorted
        return sortedVal
        
