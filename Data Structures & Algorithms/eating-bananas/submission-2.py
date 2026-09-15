class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_speed = 1
        max_speed = max(piles)
        totalTime = max_speed

        while min_speed <= max_speed:
            mid = (min_speed + max_speed) // 2

            time = 0
            for p in piles:
                time += (p + mid - 1) // mid
            
            if time <= h:
                totalTime = mid
                max_speed = mid - 1
            else:
                min_speed = mid + 1
        return totalTime
