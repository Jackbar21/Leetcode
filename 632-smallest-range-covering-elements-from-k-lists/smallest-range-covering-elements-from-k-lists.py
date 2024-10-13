class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        return self.smallestRangeHelper(nums)
        case1 = self.smallestRangeHelper(sorted(nums, key = lambda lst: lst[0]))
        case2 = self.smallestRangeHelper(sorted(nums, key = lambda lst: lst[-1]))
        case3 = self.smallestRangeHelper(sorted(nums, key = lambda lst: lst[::-1]))
        case4 = self.smallestRangeHelper(sorted(nums, key = lambda lst: lst))
        case5 = self.smallestRangeHelper(sorted(nums, key = lambda lst: lst[-1] - lst[0]))
        case6 = self.smallestRangeHelper(sorted(nums, key = lambda lst: len(lst)))
        case7 = self.smallestRangeHelper(sorted(nums, key = lambda lst: lst[0], reverse=True))
        case8 = self.smallestRangeHelper(sorted(nums, key = lambda lst: lst[-1], reverse=True))
        case9 = self.smallestRangeHelper(sorted(nums, key = lambda lst: lst[::-1], reverse=True))
        case10 = self.smallestRangeHelper(sorted(nums, key = lambda lst: lst, reverse=True))
        case11 = self.smallestRangeHelper(sorted(nums, key = lambda lst: lst[-1] - lst[0], reverse=True))
        case12 = self.smallestRangeHelper(sorted(nums, key = lambda lst: len(lst), reverse=True))

        #print(f"{case1=}, {case2=},{case3=}, {case4=},{case5=}, {case6=},")
        #print(f"{case7=}, {case8=},{case9=}, {case10=},{case11=}, {case12=},")
        return sorted(
            (cur_max - cur_min, cur_min, (cur_min, cur_max)) for (cur_min, cur_max) in [
                case1, case2, case3, case4, case5, case6, case7, case8, case9, case10, case11, case12
            ]
        )[0][2]
        return (-1, -1)
    
    def smallestRangeHelper(self, nums: List[List[int]]) -> List[int]:
        # #print(nums)
        # nums.sort(key = lambda lst: len(lst), reverse=False)
        #print(nums)
        if len(nums) == 1:
            return (nums[0][0], nums[0][0])
        # sort by (end - start, start)

        # sort by (end - start, start) as key
        # so in min_heap, store (cur_max - cur_min, cur_min, (cur_min, cur_max))
        min_heap = []

        # OPTIMIZATION to consider later: don't pick first list to pivot from,
        # pick the one with the smallest length for smallest amount of operations!
        # best_index = -1
        # best_length = len(nums[0])
        # for i in range(1, len(nums)):
        #     lst = nums[i]
        #     if len(lst) < best_length:
        #         best_length = len(lst)
        #         best_index = i
        # for num in nums[best_index]:
            # for i in range(len(nums)):
                # Skip pivot list!
                # if i == best_index:
                #     continue
                # <...REST OF CODE FROM BELOW HERE...>
        
        unique_nums = set()
        for lst in nums:
            # for num in [lst[0], lst[len(lst)//2 - 1], lst[len(lst)//2], lst[len(lst)//2 -2], lst[-1]]:
            for index in [
                0, len(lst)//2 - 2, len(lst)//2 - 1, len(lst)//2, len(lst)//2 + 1, len(lst) - 1
            ]:
                if 0 <= index < len(lst):
                    unique_nums.add(lst[index])
        
        
        for pivot_num in unique_nums: # k * 50
            # if pivot_num == 20:
                #print("TRUEEEEE")
            cur_min, cur_max = pivot_num, pivot_num
            #print(f"num={pivot_num}")
            # for i in range(1, len(nums)):
            #     lst = nums[i]
            for lst in nums: # k
                closest_num = self.getClosestNum(lst, pivot_num) # log(50)
                # #print(pivot_num, cur_min, cur_max)
                # closest_small = self.getClosestSmallerNum(lst, cur_min)
                # #print(f"{closest_small=}")
                # closest_large = self.getClosestLargerNum(lst, cur_max)
                # #print(f"{closest_large=}")
                # #print()

                # if abs(cur_min - closest_small) <= abs(cur_max - closest_large):
                #     cur_min = min(cur_min, closest_small)
                # else:
                #     cur_max = max(cur_max, closest_large)

                cur_min = min(cur_min, closest_num)
                cur_max = max(cur_max, closest_num)
            #print((cur_min, cur_max))
            heapq.heappush(min_heap,
                (cur_max - cur_min, cur_min, (cur_min, cur_max))
            )
            #print()
        
        #print(min_heap)
        # return (-1, -1)
        return min_heap[0][2]
    
    def getClosestSmallerNum(self, sorted_list, target):
        # Find index i of largest number in sorted_list
        # such that sorted_list[i] <= target
        # pass
        if sorted_list[0] >= target:
            return sorted_list[0]
        l, r = 0, len(sorted_list) - 1
        rightmost_index = -1
        while l <= r:
            mid = (l + r) // 2
            if sorted_list[mid] <= target:
                # r = mid - 1
                l = mid + 1
                rightmost_index = max(rightmost_index, mid)
            else:
                # l = mid + 1
                r = mid - 1
        
        assert rightmost_index > -1
        return sorted_list[rightmost_index]

    
    def getClosestLargerNum(self, sorted_list, target):
        # Find index i of smallest number in sorted_list
        # such that sorted_list[i] >= target
        if sorted_list[-1] <= target:
            return sorted_list[-1]
        l, r = 0, len(sorted_list) - 1
        leftmost_index = len(sorted_list)
        while l <= r:
            mid = (l + r) // 2
            if sorted_list[mid] >= target:
                r = mid - 1
                leftmost_index = min(leftmost_index, mid)
            else:
                l = mid + 1
        
        # return l
        assert leftmost_index < len(sorted_list)
        # return leftmost_index
        return sorted_list[leftmost_index]

                
    def getClosestNum(self, sorted_list, target):
        # Return closest number to target, favoring smaller numbers
        # in case of ties, from sorted_list.

        # Case 1: target <= sorted_list[0]
        if target <= sorted_list[0]:
            #print(f"CASE1, res={sorted_list[0]}")
            return sorted_list[0]

        # Case 2: sorted_list[-1] <= target
        if sorted_list[-1] <= target:
            #print(f"CASE2, res={sorted_list[-1]}")
            return sorted_list[-1]

        # Case 3: find leftmost index i such that
        # target < sorted_list[i]
        l, r = 0, len(sorted_list) - 1

        while l <= r:
            mid = (l + r) // 2
            if sorted_list[mid] == target:
                return target
            
            if target < sorted_list[mid]:
                r = mid - 1
            else:
                assert sorted_list[mid] < target
                l = mid + 1
        
        # l == leftmost index
        assert target < sorted_list[l]
        if l - 1 >= 0:
            assert target > sorted_list[l - 1]
        
        
        # #print(sorted_list, l, sorted_list[l])
        # Between index l and index l - 1, return closest
        # one to target. In case of tie, return num at l-1 index
        assert l - 1 >= 0 # Might not be true...
        # if l == 0:
        #     return sorted_list[l]
        res = sorted_list[l - 1]
        if abs(sorted_list[l] - target) < abs(sorted_list[l - 1] - target):
            res = sorted_list[l]
        #print(sorted_list, sorted_list[l - 1], sorted_list[l], f"{res=}")
        # #print(target, )
        return res
        return sorted_list[l] # TODO: fix this


        # 3500 * 50 == 3500 * 100 / 2 == 350_000 / 2
        # == 175_000 == 1.75 * 10^5

        # Case 1:
        # L1 - 4
        # L2 - 0,9 -> 0
        # L3 - 5
        # ANS: [0,5]

        # Case 2:
        # L1 - 10
        # L2 - 9,12 -> 9
        # L3 - 5,18 -> 5
        # ANS: [5, 10]

        # Case 3:
        # L1 - 15
        # L2 - 12,20 -> 12
        # L3 - 5,18 -> 18
        # ANS: [12, 18]

        # Case 4:
        # L1 - 24
        # L2 - 20
        # L3 - 22,30 -> 22
        # ANS: [20, 24]

        # Case 5:
        # L1 - 26
        # L2 - 20
        # L3 - 22,30 -> 22
        # ANS: [20, 26]