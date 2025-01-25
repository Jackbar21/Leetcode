class Solution:
    def intervalsOverlap(self, i1, i2):
        s1, e1 = i1
        s2, e2 = i2

        assert s1 <= e1
        assert s2 <= e2

        if s1 > s2:
            return self.intervalsOverlap(i2, i1)
        
        assert s1 <= s2
        if s1 == s2:
            return True
        
        assert s1 < s2
        if e1 < s2:
            return False
        
        return True

    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        N = len(nums)
        NUM, INDEX = 0, 1
        sorted_nums = sorted((num, i) for i, num in enumerate(nums))
        connected_components = []
        d = {}

        i = 0
        while i < N:
            # Create new connected component
            num, num_index = sorted_nums[i]
            lower, upper = num - limit, num + limit
            i += 1
            connected_component = [num]
            d[num_index] = connected_component
            # while i < N and self.intervalsOverlap((lower, upper), (sorted_nums[i][NUM] - limit, sorted_nums[i][NUM] + limit)):
            while i < N:
                sorted_num, sorted_index = sorted_nums[i]

                # Check if "overlapping"
                if not (lower <= sorted_num <= upper):
                    break
                
                # TODO: maybe swap min/max functions? Probably not!
                lower = min(lower, sorted_num - limit)
                upper = max(upper, sorted_num + limit)

                # connected_component.append(sorted_nums[i][NUM])
                # d[sorted_nums[i][INDEX]] = connected_component
                # i += 1
                connected_component.append(sorted_num)
                d[sorted_index] = connected_component
                i += 1
            
            connected_component.reverse()
            connected_components.append(connected_component)
        
        # print(f"{d=}")
        # print(f"{connected_components=}")
        # return []
        return [d[i].pop() for i in range(N)]

                
