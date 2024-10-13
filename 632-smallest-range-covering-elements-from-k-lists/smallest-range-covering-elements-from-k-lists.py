class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        if len(nums) == 1:
            return (nums[0][0], nums[0][0])
        # elif max(map(lambda lst: len(lst), nums)) == 1:
        #     return (
        #         min(lst[0] for lst in nums),
        #         max(lst[-1] for lst in nums)
        #     )


        NUM, INDEX = 0, 1
        d = {lst_index: 0 for lst_index in range(len(nums))}
        sorted_list = sorted((num, i) for i in range(len(nums)) for num in nums[i])
        #print(sorted_list, f"{len(sorted_list)=}")
        l, r = 0,0
        d[sorted_list[0][INDEX]] += 1
        # res = [float("-inf"), float("inf")]
        # min_heap = [sorted_list[0][NUM]]
        # max_heap = [sorted_list[0][NUM]]
        res = [float("inf"), float("-inf")]
        results = []
        while l < len(sorted_list):
            assert l <= r
            # if not l <= r:
            #     #print("ALERT!!!", l, r)
            # #print(needed, d)
            needed = set(i for i in d if d[i] == 0)
            while len(needed) > 0 and r + 1 < len(sorted_list):
                r += 1
                if sorted_list[r][INDEX] in needed:
                    needed.remove(sorted_list[r][INDEX])
                d[sorted_list[r][INDEX]] += 1
                res[-1] = max(res[-1], sorted_list[r][NUM])
                

                # res[-1] = max(res[-1], sorted_list[r][NUM])
            #print(f"{needed=}, {d=}, {r + 1 < len(sorted_list)=}, {len(needed) > 0=}")
            
            while d[sorted_list[l][INDEX]] > 1:
                #print(l, r, d)
                d[sorted_list[l][INDEX]] -= 1
                l += 1
                
                res[0] = min(res[0], sorted_list[l][INDEX])
            
            #print(f"{l,r=}, {sorted_list[l], sorted_list[r]=}")
            if all(d[i] > 0 for i in d):
                results.append([sorted_list[l][NUM], sorted_list[r][NUM]])

            if r + 1 >= len(sorted_list):
                assert r + 1 == len(sorted_list)
                #print(f"{results=}")
                if len(results) > 0:
                    return sorted(results, key = lambda interval: (interval[1] - interval[0], interval[0]))[0]
                
                return [1,1]
                return res

            # Move forward (Loop Invariant)
            d[sorted_list[l][INDEX]] -= 1
            l += 1




        # #print(sorted_list)
        #print(f"{results=}")
        return sorted(results, key = lambda interval: (interval[1] - interval[0], interval[0]))[0]
        # return [1,2]