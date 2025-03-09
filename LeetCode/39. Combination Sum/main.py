from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, path, res):
            if target == 0:
                res.append(path)
                return
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break
                backtrack(i, target - candidates[i], path + [candidates[i]], res)
        
        candidates.sort()
        res = []
        backtrack(0, target, [], res)
        return res