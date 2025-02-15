from typing import List
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def mergeSort(nums, left, right):
            if left >= right:
                return 0
            mid = (left + right) // 2
            count = mergeSort(nums, left, mid) + mergeSort(nums, mid + 1, right)
            
            j = mid + 1
            for i in range(left, mid + 1):
                while j <= right and nums[i] > 2 * nums[j]:
                    j += 1
                count += (j - (mid + 1))
            
            temp = []
            i, j = left, mid + 1
            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
            while i <= mid:
                temp.append(nums[i])
                i += 1
            while j <= right:
                temp.append(nums[j])
                j += 1
            nums[left:right + 1] = temp
            
            return count
        
        return mergeSort(nums, 0, len(nums) - 1)
