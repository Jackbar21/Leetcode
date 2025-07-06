class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2

        freqs = {}
        for num2 in nums2:
            freqs[num2] = freqs.get(num2, 0) + 1
        self.freqs = freqs


    def add(self, index: int, val: int) -> None:
        nums2, freqs = self.nums2, self.freqs

        # Delete old number
        num = nums2[index]
        freqs[num] -= 1

        # Update new number
        new_num = num + val
        nums2[index] = new_num
        freqs[new_num] = freqs.get(new_num, 0) + 1

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
            res += freqs.get(desired_num2, 0)
        return res
