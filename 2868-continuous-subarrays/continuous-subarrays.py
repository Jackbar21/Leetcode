class Solution:
    def isValidDict(self, d):
        if len(d) > 3:
            return False

        # At most 3 elements, need to make sure that they're all at most 2 away from each other!
        for key1 in d:
            for key2 in d:
                if abs(key1 - key2) > 2:
                    return False
        
        return True

    def continuousSubarrays(self, nums: List[int]) -> int:
        d = defaultdict(int)
        count = 0
        double_count = 0

        l = 0
        for r, num in enumerate(nums):
            # # print(f"{d=}, {self.isValidDict(d)=}")
            d[num] += 1
            if self.isValidDict(d):
                continue
            
            double_count += 1
            # nums[l..r] is invalid, but nums[l..r-1] is valid! Therefore, it must be that
            # EVERY non-empty subarray within nums[l..r-1] is ALSO valid! We know the length
            # of this array is (r-1)-l+1 == r-l, and so total number of subarrays will be
            # r-l subarrays of length 1 + r-l-1 subarrays of length 2 + ... + 1 subarray of
            # length r - l == r-l + r-l-1 + ... + 1 == (r-l)(r-l+1)/2, by math :)
            n = (r - l)
            length = n
            # count += (n * (n + 1)) // 2
            while not self.isValidDict(d):
                l_num = nums[l]
                d[l_num] -= 1
                assert d[l_num] >= 0
                if d[l_num] == 0:
                    del d[l_num]
                l += 1
                count += length
                length -= 1
                assert length >= 0

            continue
        
        n = len(nums) - l
        # print(f"FINALL: {d=}, {count=}, {l=}, {n * (n + 1) // 2}, {double_count=}")
        return count + n * (n + 1) // 2

        