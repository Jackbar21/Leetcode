class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low == high:
            return int(low % 2 == 1)

        if low % 2 == high % 2:
            return (low % 2 == 1) + self.countOdds(low + 1, high)
        
        # Either low & high are even & odd or odd & even
        # In either case, there 1 + (high - low) // 2 odd numbers
        return 1 + (high - low) // 2
