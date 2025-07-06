class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2

        self.freqs = defaultdict(int)
        for num in nums2:
            self.freqs[num] += 1


    def add(self, index: int, val: int) -> None:
        # Delete old number
        num = self.nums2[index]
        self.freqs[num] -= 1
        assert self.freqs[num] >= 0

        # Update new number
        self.nums2[index] += val
        self.freqs[num + val] += 1

    def count(self, tot: int) -> int:
        # For each number 'num1' in nums1, we want some number 'num2' in nums2
        # such that num1 + num2 == tot. This implies that num2 == tot - num1
        # Hence we can loop through each number in nums1, and use our freqs
        # dictionary to check if needed number exists (and if so, add to count
        # the number of times that number exists in nums2!)
        res = 0
        for num1 in self.nums1:
            desired_num2 = tot - num1
            assert (count := self.freqs[desired_num2]) >= 0
            res += count
        return res
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)