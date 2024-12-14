class Solution:
    def isValidDict(self, d):
        if len(d) > 3:
            return False
        
        # At most 3 elements, need to make sure that they're all at most 2 away from each other!
        keys = list(d.keys())
        for i in range(len(keys)):
            for j in range(len(keys)):
                if abs(keys[i] - keys[j]) > 2:
                    return False
        
        return True


    def continuousSubarrays(self, nums: List[int]) -> int:
        d = defaultdict(int)
        count = 0
        double_count = 0

        l = 0
        for r, num in enumerate(nums):
            # print(f"{d=}, {self.isValidDict(d)=}")
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
        print(f"FINALL: {d=}, {count=}, {l=}, {n * (n + 1) // 2}, {double_count=}")
        return count + n * (n + 1) // 2

        #     # print(d)
        #     # dict_changed = False
        #     print(f"{d=}, {self.isValidDict(d)=}")
        #     if not self.isValidDict(d):
        #         double_count += 1
        #         # current subarray represents nums[l..r], and introducing
        #         # num at index r just "broke" the continuous property. Hence,
        #         # we know that every subarray nums[l..j], where l < j < r, are
        #         # valid, and hence we count them! Then, we will start at next
        #         # available l :)

        #         # For counting, we know that nums[l..l] is valid, nums[l..l+1] is valid,
        #         # nums[l..l+2] is valid, ..., nums[l..r-1] is valid. Hence in total, there
        #         # are (r-1)-l+1 == r - l valid subarrays!
        #         # CORRECTION: For counting, we know that there are (r - l) valid subarrays
        #         # of length 1, (r - l - 1) valid subarrays of length 2, ..., 1 valid subarray
        #         # of length (r - l)
        #         assert l <= r - 1
        #         print(f"{count=}, {r - l=}, {l=}, {r=}")
        #         n = (r - l)
        #         print(f"{count=}, {(n * (n + 1)) // 2=}")
        #         count += (n * (n + 1)) // 2 

        #         while not self.isValidDict(d):
        #             assert l < r
        #             l_num = nums[l]
        #             d[l_num] -= 1
        #             assert d[l_num] >= 0
        #             if d[l_num] == 0:
        #                 del d[l_num]
        #             l += 1
        #         assert l <= r and self.isValidDict(d) # Strong statement!
        #         print(f"POST COUNT: {l=}")
        #         # count += r - l + 1
        #     # else:
        #     #     count += 1
        #     # print(f"{d=}, {self.isValidDict(d)=}")
        #     # print("\n")

        #     # if dict_changed:
        #     #     # (r - l + 1) + (r - l) + (r - l - 1) + ... + 1
        #     #     # == (r - l + 1)(r - l + 2) // 2
        #     #     count += (r - l + 1) * (r - l + 2) // 2
        #     # else:
        #     #     count += 1
        
        # # print(f"{d=}, {self.isValidDict(d)=}")
        # # if len(d) > 0 and self.isValidDict(d):
        # #     count += len(d) + 1
        # # r = len(nums)
        # # if not self.isValidDict(d):
        # #     # current subarray represents nums[l..r], and introducing
        # #     # num at index r just "broke" the continuous property. Hence,
        # #     # we know that every subarray nums[l..j], where l < j < r, are
        # #     # valid, and hence we count them! Then, we will start at next
        # #     # available l :)

        # #     # For counting, we know that nums[l..l] is valid, nums[l..l+1] is valid,
        # #     # nums[l..l+2] is valid, ..., nums[l..r-1] is valid. Hence in total, there
        # #     # are (r-1)-l+1 == r - l valid subarrays!
        # #     print(f"{count=}, {r - l=}")
        # #     # count += r - l
        # #     count += ((r - l) * (r - l + 1)) // 2

        # #     while l < r and not self.isValidDict(d):
        # #         l_num = nums[l]
        # #         d[l_num] -= 1
        # #         if d[l_num] == 0:
        # #             del d[l_num]
        # #         l += 1
        # #     assert l <= r and self.isValidDict(d) # Strong statement!
        # #     # count += ((r - l) * (r - l + 1)) // 2
        
        # n = len(nums) - l
        # print(f"FINAL: {count=}, {(n * (n + 1)) // 2=}")
        # print(f"{count}, {(len(nums) - l + 1 - 1 - 1) * (len(nums) - l + 2 - 1 - 1) // 2}, {double_count=}")
        # return count + ((n * (n + 1)) // 2) - 0


