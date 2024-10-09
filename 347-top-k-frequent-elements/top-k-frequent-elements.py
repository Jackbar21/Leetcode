class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Edge cases: 
        #   (1) nums is same num n times, so min freq is len(nums)
        #   (2) only unique num in nums, so max freq is 1
        #   Hence, every number in nums will have a frequency between 1 and len(nums) [inclusive]
        freq_dict = {i: set() for i in range(len(nums) + 1)} # freq to num

        d = {} # num to freq
        for num in nums:
            freq = d.get(num, 0) + 1
            d[num] = freq
            if num in freq_dict[freq - 1]:
                freq_dict[freq - 1].remove(num)
            assert num not in freq_dict[freq]
            freq_dict[freq].add(num)
            
        assert len(freq_dict[0]) == 0
        res = []
        for freq in range(len(nums), 0, -1):
            # Done with problem
            if k <= 0:
                break
            
            # Add whole values at frequency freq
            # if enough space to add them all
            if k >= len(freq_dict[freq]):
                res.extend(freq_dict[freq])
                k -= len(freq_dict[freq])
                continue

            # k is smaller than list of values at freq_dict[freq]
            # so pop one by one until reach end
            while k > 0:
                res.append(freq_dict[freq].pop())
                k -= 1
            assert k == 0
            return res
        
        assert k == 0
        return res