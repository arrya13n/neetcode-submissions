class Solution:
    def trap(self, height: List[int]) -> int:
        # if not height:
        #     return 0
        
        # l,r = 0, len(height)-1
        # lmax,rmax = 0,0
        # result = 0

        # while l < r:
        #     lmax = max(lmax,height[l])
        #     rmax = max(rmax,height[r])

        #     if lmax < rmax:
        #         result += lmax - height[l]
        #         l += 1 
        #     else:
        #         result += rmax - height[r]
        #         r -= 1
        # return result

        #prefix-suffix array
        if not height:
            return 0
        lmax = [0] * len(height)
        rmax = [0] * len(height)

        lmax[0] = height[0]
        for i in range(1,len(height)):
            lmax[i] = max(lmax[i-1],height[i])
        
        rmax[len(height)-1] = height[len(height)-1]
        for i in range(len(height)-2,-1,-1):
            rmax[i] = max(rmax[i+1], height[i])
        
        result = 0
        for i in range(len(height)):
            result += min(lmax[i],rmax[i]) - height[i]
        return result
