class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        cur_min, cur_max = float("inf"), float("-inf")
        min_index, max_index = -1, -1

        for i in range(len(arrays)):
            small, big = arrays[i][0], arrays[i][-1]
            if small < cur_min:
                cur_min = small
                min_index = i
            
            # second clause in if statement not relevent asymptotically
            # if big > cur_max or min_index != max_index:
            if big > cur_max:
                cur_max = big
                # if not (big == cur_max and min_index == i):
                max_index = i
        
        if min_index != max_index:
            return cur_max - cur_min
        
        # Min and max values are inside the same array.
        # So best result is to either keep cur_min and find max amongst other arrays,
        # OR keep cur_max and find min amongst other arrays.
        second_best_min, second_best_max = float("inf"), float("-inf")
        assert min_index == max_index
        banned_index = min_index

        for i in range(len(arrays)):
            if i == banned_index:
                continue

            small, big = arrays[i][0], arrays[i][-1]
            second_best_min = min(second_best_min, small)
            second_best_max = max(second_best_max, big)
            
        
        case1 = cur_max - second_best_min
        case2 = second_best_max - cur_min
        return max(case1, case2)



        # Case 1: min and max value are in different arrays

        # Case 2: min and max value are in same array
            # Either grab max value from OTHER arrays
            # OR grab min value from OTHER arrays
            # for each of tehse two cases, take the one whose 
            # difference will yield a larger result

