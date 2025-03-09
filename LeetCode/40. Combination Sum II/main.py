from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, path, res):
            if target == 0:
                res.append(path)
                return
            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                # Stop if the candidate is greater than the remaining target
                if candidates[i] > target:
                    break
                # Move to the next candidate to avoid reusing the same candidate
                backtrack(i + 1, target - candidates[i], path + [candidates[i]], res)
        
        candidates.sort()
        res = []
        backtrack(0, target, [], res)
        return res