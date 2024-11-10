class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        smallest_k = 1
        largest_k = max(piles)

        while smallest_k <= largest_k:
            k = (smallest_k + largest_k) // 2

            # Check if CAN eat all bananas in k bananas-per-hour
            # I.e. figure out how many hours it takes to eat ALL the
            # bananas at a rate of k bananas-per-hour, and check if
            # it it <= h (which is when the guards come back)
            num_hours = sum(math.ceil(banana_pile / k) for banana_pile in piles)
            if num_hours <= h:
                largest_k = k - 1
            else:
                smallest_k = k + 1
        
        return smallest_k