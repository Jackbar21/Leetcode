class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        N = len(nums)
        distinct_count = len(set(nums))

        res = 0
        for i in range(len(nums)):
            distinct = set()
            for j in range(i, N):
                distinct.add(nums[j])
                if len(distinct) == distinct_count:
                    res += N - j
                    break
                # res += len(distinct) == distinct_count
        return res
            
        

        # O(N) - but incorrect
        l = 0
        d = {}
        res = 0
        for r, num in enumerate(nums):
            d[num] = d.get(num, 0) + 1

            while len(d) == distinct_count:
                res += N - r
                for idx in range(r, N):
                    print(f"{nums[l:idx+1]}")
                l_num = nums[l]
                d[num] -= 1
                if d[num] == 0:
                    del d[num]
                l += 1
       
        return res