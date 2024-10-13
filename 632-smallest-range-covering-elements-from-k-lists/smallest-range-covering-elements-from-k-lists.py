class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        if len(nums) == 1:
            return (nums[0][0], nums[0][0])

        NUM, INDEX = 0, 1
        d = {lst_index: 0 for lst_index in range(len(nums))}
        sorted_list = sorted((num, i) for i in range(len(nums)) for num in nums[i])

        l, r = 0,0
        d[sorted_list[0][INDEX]] += 1

        # Precompute first round
        needed = set(i for i in d if d[i] == 0)
        results = []
        while len(needed) > 0 and r + 1 < len(sorted_list):
            r += 1
            if sorted_list[r][INDEX] in needed:
                needed.remove(sorted_list[r][INDEX])
            d[sorted_list[r][INDEX]] += 1

        # Must exist at least one solution!
        # assert len(needed) == 0
        

        while d[sorted_list[l][INDEX]] > 1:
            d[sorted_list[l][INDEX]] -= 1
            l += 1
        
        # results.append([sorted_list[l][NUM], sorted_list[r][NUM]])
        interval = [sorted_list[l][NUM], sorted_list[r][NUM]]
        heapq.heappush(results, (interval[1] - interval[0], interval[0], interval))

        needed_index = sorted_list[l][INDEX]
        d[needed_index] -= 1
        # assert d[needed_index] == 0
        l += 1

        while l < len(sorted_list):
            # assert l <= r
            
            found_needed_index = False
            while r + 1 < len(sorted_list):
                r += 1
                d[sorted_list[r][INDEX]] += 1
                if sorted_list[r][INDEX] == needed_index:
                    found_needed_index = True
                    break
            
            # If didn't find needed index, no more solutions exist, hence return!
            if not found_needed_index:
                # return sorted(results, key = lambda interval: (interval[1] - interval[0], interval[0]))[0]
                return results[0][2]
            
            while d[sorted_list[l][INDEX]] > 1:
                d[sorted_list[l][INDEX]] -= 1
                l += 1
            
            # results.append([sorted_list[l][NUM], sorted_list[r][NUM]])
            interval = [sorted_list[l][NUM], sorted_list[r][NUM]]
            heapq.heappush(results, (interval[1] - interval[0], interval[0], interval))

            needed_index = sorted_list[l][INDEX]
            d[needed_index] -= 1
            # assert d[needed_index] == 0
            l += 1
        
        raise Exception("Unreachable Code")
