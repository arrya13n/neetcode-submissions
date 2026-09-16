class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def dfs(i, curr_var, total):
            if total == target:
                result.append(curr_var.copy())
                return

            for j in range(i, len(candidates)):
                if total + candidates[j] > target:
                    break

                # Skip duplicate choices at the same level
                if j > i and candidates[j] == candidates[j - 1]:
                    continue

                curr_var.append(candidates[j])

                # j + 1 because each number can only be used once
                dfs(j + 1, curr_var, total + candidates[j])

                curr_var.pop()

        dfs(0, [], 0)
        return result