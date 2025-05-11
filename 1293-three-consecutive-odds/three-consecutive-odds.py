class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        is_odd = lambda num: num % 2 == 1
        three_consecutive = lambda i: is_odd(arr[i - 1]) and is_odd(arr[i]) and is_odd(arr[i + 1])
        return any(three_consecutive(index) for index in range(1, len(arr) - 1))