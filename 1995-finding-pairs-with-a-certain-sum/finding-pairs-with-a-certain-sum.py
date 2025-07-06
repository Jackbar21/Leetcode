class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2

        freqs = defaultdict(int)
        for num2 in nums2:
            freqs[num2] += 1
        self.freqs = freqs


    def add(self, index: int, val: int) -> None:
        nums2, freqs = self.nums2, self.freqs

        # Delete old number
        num = nums2[index]
        freqs[num] -= 1

        # Update new number
        nums2[index] += val
        freqs[num + val] += 1

    def count(self, tot: int) -> int:
        nums1, freqs = self.nums1, self.freqs

        # For each number 'num1' in nums1, we want some number 'num2' in nums2
        # such that num1 + num2 == tot. This implies that num2 == tot - num1
        # Hence we can loop through each number in nums1, and use our freqs
        # dictionary to check if needed number exists (and if so, add to count
        # the number of times that number exists in nums2!)
        res = 0
        for num1 in nums1:
            desired_num2 = tot - num1
            assert (count := freqs[desired_num2]) >= 0
            res += count
        return res
