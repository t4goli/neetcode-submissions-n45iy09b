class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if not piles:
            return -1

        low, high = 1, max(piles)

        while low <= high:
            mid = (low + high) // 2
            hours = 0
            for pile in piles:
                if pile % mid == 0:
                    hours += int(pile / mid)
                else:
                    hours += int((pile/mid) + 1)

            if hours <= h:
                high = mid - 1
            else:
                low = mid + 1

        return low