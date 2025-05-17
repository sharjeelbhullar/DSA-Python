from typing import List
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        ans = []
        
        for i in range(len(nums)):
            # Remove elements outside the current window
            if dq and dq[0] == i - k:
                dq.popleft()

            # Remove elements smaller than the current one from the back
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            # Append the maximum of the current window
            if i >= k - 1:
                ans.append(nums[dq[0]])
        
        return ans