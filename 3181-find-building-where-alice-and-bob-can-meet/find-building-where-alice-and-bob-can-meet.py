class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        # Suppose without loss of generality, that a_i <= b_i. Then answer is either:
        # b_i, OR
        # first j such that height[j] > max(heights[a_i], heights[b_i])

        # prefix_heights[i] == index of first index j > i such that heighs[j] > heights[i]
        prefix_heights = [-1] * len(heights)
        stack = [] # monotonically-decreasing stack
        HEIGHT, INDEX = 0, 1
        for i, height in enumerate(heights):
            while len(stack) > 0 and height > stack[-1][HEIGHT]:
                smaller_height, smaller_index = stack.pop()
                assert prefix_heights[smaller_index] == -1
                prefix_heights[smaller_index] = i
            stack.append((height, i))
        
        # print(f"{stack=}")
        # print(f"{prefix_heights}")
        # return []

        # Suppose without loss of generality, that a_i <= b_i. Then answer is either:
        # b_i, OR
        # first j such that height[j] > max(heights[a_i], heights[b_i])
        ans = []
        # for a, b in queries:
        @cache
        def querySolver(min_index, max_index):
            if min_index == -1 or max_index == -1:
                return -1
    
            if min_index > max_index:
                return querySolver(max_index, min_index)

            if min_index == max_index:
                return max_index
            
            if heights[min_index] < heights[max_index]:
                return max_index
            else:
                return querySolver(min_index, prefix_heights[max_index])

            # min_index, max_index = a, b
            # if min_index > max_index:
            #     min_index, max_index = max_index, min_index
            # if heights[min_index] < heights[max_index]:
            #     return max_index
            
            # height_to_beat = heights[min_index]
            # index = max_index

            # if index != -1 and heights[index] <= height_to_beat
            # while index != -1 and heights[index] <= height_to_beat:
            #     index = prefix_heights[index]
            # return index
            # ans.append(index)
            # max_height_index = a if heights[a] > heights[b] else b
            # print(f"{max_height_index=}, {a=}, {b=}, {heights[a]=}, {heights[b]=}")
            # leftmost_index = prefix_heights[max_height_index]
            # ans.append(leftmost_index)
            # continue
        
        # return ans
        return [querySolver(a, b) for (a, b) in queries]
