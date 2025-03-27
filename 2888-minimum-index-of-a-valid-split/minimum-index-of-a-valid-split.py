class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        N = len(nums)

        # Step 1: Build num-to-frequency dictionary of nums
        d = defaultdict(int)
        for num in nums:
            d[num] += 1

        # Step 2: Get dominant element & frequency count
        dom_element, dom_freq = nums[0], 1 
        for num, freq in d.items():
            if dom_freq < freq:
                dom_freq = freq
                dom_element = num

        # Step 3: Find first partition that yields dominant element
        # in both subarrays.
        dom_count = 0
        for i, num in enumerate(nums):
            cur_count = i + 1
            dom_count += (num == dom_element)

            # Check if element is currently dominant
            if 2 * dom_count > cur_count:
                # Get dom_element count & overall count in second subarray partition
                other_dom_count = dom_freq - dom_count
                other_cur_count = N - cur_count

                if 2 * other_dom_count > other_cur_count:
                    # dom_element is dominant in both nums[0..i] and nums[i+1..N-1]
                    # and was not for any index smaller than i. Hence, index i must
                    # be the minimum index of a valid split!
                    return i
        
        return -1
