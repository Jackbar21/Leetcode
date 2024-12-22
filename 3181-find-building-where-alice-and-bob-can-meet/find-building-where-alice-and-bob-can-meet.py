class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        # prefix_heights[i] == index of first index j > i such that heighs[j] > heights[i]
        prefix_heights = [-1] * len(heights)
        stack = [] # monotonically-decreasing stack
        HEIGHT, INDEX = 0, 1
        for i, height in enumerate(heights):
            while len(stack) > 0 and height > stack[-1][HEIGHT]:
                smaller_height, smaller_index = stack.pop()
                prefix_heights[smaller_index] = i
            stack.append((height, i))
        
        # Suppose without loss of generality, that a_i <= b_i. Then answer is either:
        # b_i, OR
        # first j such that height[j] > max(heights[a_i], heights[b_i])
        @cache
        def querySolver(min_idx, max_idx):
            if max_idx == -1 or heights[min_idx] < heights[max_idx]:
                return max_idx
            return querySolver(min_idx, prefix_heights[max_idx])
        
        return [
            querySolver(a, b) if a < b 
            else querySolver(b, a) if a > b
            else b # They're the same index, so don't move!
            for (a, b) in queries
        ]