class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left_half,right_half) -> List[int]:
            i = 0
            j = 0
            ans = []
            while i < len(left_half) and j < len(right_half):
                
                if left_half[i] <= right_half[j]:
                    ans.append(left_half[i])
                    i += 1
                else:
                    ans.append(right_half[j])
                    j += 1
            ans.extend(left_half[i:])
            ans.extend(right_half[j:])

            return ans

        def mergeSort(left, right, arr):
            if left == right:
                return [arr[left]]
            mid = (left + right) //2
            left_half = mergeSort(left, mid, arr)
            right_half = mergeSort(mid + 1, right, arr)
        
            return merge(left_half, right_half)

        return mergeSort(0, len(nums) - 1, nums)
