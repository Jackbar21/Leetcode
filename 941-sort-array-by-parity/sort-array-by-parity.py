class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even,odd = [],[]
        for num in nums:
            (odd if num%2 else even).append(num)
        return even + odd