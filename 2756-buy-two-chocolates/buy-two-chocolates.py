class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        m, index = float("inf"), -1
        
        for i in range(len(prices)):
            if prices[i] < m:
                m = prices[i]
                index = i
        
        n = float("inf")
        for i in range(len(prices)):
            if prices[i] < n and i != index:
                n = prices[i]
        
        if n + m > money:
            return money
        return money - n - m