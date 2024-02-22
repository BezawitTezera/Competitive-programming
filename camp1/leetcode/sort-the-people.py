class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        NewDict = {}
        arr = []
        for i in range(len(heights)):
            NewDict[heights[i]] = names[i]
        new = sorted(NewDict.keys(), reverse = True)
        for val in new:
            arr.append(NewDict[val])
        return arr