class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        stack = []
        d = defaultdict(lambda:-1)
        for num in nums2:
            while stack and num > stack[-1]:
                d[stack[-1]] = num
                stack.pop()
            stack.append(num)
        
        for val in nums1:
            ans.append(d[val])
        return ans
                
