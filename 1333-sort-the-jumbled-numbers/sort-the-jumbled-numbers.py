class Solution:
    def __init__(self):
        self.mapping = None
    def mapNum(self, num):
        return int(''.join(str(self.mapping[int(str_digit)]) for str_digit in str(num)))
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        self.mapping = mapping
        return sorted(nums, key=lambda num:(self.mapNum(num)))