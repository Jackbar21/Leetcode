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
            # freq = num_to_freq[num]
            
        assert len(freq_dict[0]) == 0
        res = []
        for freq in range(len(nums), 0, -1):
            while k > 0 and len(freq_dict[freq]) > 0:
                res.append(freq_dict[freq].pop())
                k -= 1
            if k == 0:
                return res
        
        assert k == 0
        return res




        
        # return sorted(set(nums), key=lambda num: d[num])[-k:]
        max_heap = []
        for num in d:
            heapq.heappush(max_heap, (-d[num], num))
        
        # O(klogn), k <= n
        heapq.heapify(max_heap) # O(n)
        res = []
        for _ in range(k): # O(k)
            res.append(heapq.heappop(max_heap)[1]) # O(logn)
        return res