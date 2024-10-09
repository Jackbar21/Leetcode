class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # num-to-frequency dict
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1

        # Edge cases: 
        #   (1) nums is same num n times, so min freq is len(nums)
        #   (2) only unique num in nums, so max freq is 1
        #   Hence, every number in nums will have a frequency between 1 and len(nums) [inclusive]
        freq_dict = {i: set() for i in range(1, len(nums) + 1)} # freq to num

        # Add all nums to appropriate frequency set.
        for num in d:
            freq = d[num]
            freq_dict[freq].add(num)
        
        res = []
        for freq in range(len(nums), 0, -1):
            # Done with problem
            if len(res) == k:
                break
            
            # Add whole values at frequency freq
            # if enough space to add them all
            if k - len(res) >= len(freq_dict[freq]):
                res.extend(freq_dict[freq])
                continue

            # k is smaller than list of values at freq_dict[freq]
            # so pop one by one until reach end
            while len(res) < k:
                res.append(freq_dict[freq].pop())
            return res
        
        assert len(res) == k
        return res