class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        pre = 1
        for i in range(len(nums)):
            result[i] = pre
            pre *= nums[i]
        
        suf = 1
        for i in reversed(range(len(nums))):
            result[i] *= suf
            suf *= nums[i]
        
        return result