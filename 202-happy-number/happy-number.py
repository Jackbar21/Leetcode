class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        num = n
        while num not in seen:
            seen.add(num)
            num = sum(map(lambda x:x*x, [int(i) for i in str(num)]))
            if num == 1:
                return True
        
        # num found in seen, so infinite cycle detected
        return False