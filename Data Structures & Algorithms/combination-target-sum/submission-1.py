class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()

        def dfs(i,current_combo, total):
            if total == target:
                result.append(current_combo.copy())
                return
            
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                
                current_combo.append(nums[j])
                dfs(j, current_combo, total+nums[j])
                current_combo.pop()
        dfs(0,[],0)
        return result