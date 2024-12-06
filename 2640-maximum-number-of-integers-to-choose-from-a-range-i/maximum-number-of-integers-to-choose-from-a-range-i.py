class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_set = set(banned)

        count = 0
        for num in range(1, n + 1):
            if num > maxSum:
                break
            if num not in banned_set:
                maxSum -= num
                count += 1

        return count
        
        
