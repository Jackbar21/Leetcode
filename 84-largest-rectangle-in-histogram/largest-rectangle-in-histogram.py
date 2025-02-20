class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # I read Neetcode's hints, and developed this O(N) solution from it!
        N = len(heights)
        INDEX, HEIGHT = 0, 1

        next_non_smallest = [N - 1] * N
        stack = [(None, float("-inf"))]
        for index, height in enumerate(heights):
            while height < stack[-1][HEIGHT]:
                prev_index, _ = stack.pop()
                next_non_smallest[prev_index] = index - 1
            stack.append((index, height))
        
        prev_non_smallest = [0] * N
        stack = [(None, float("-inf"))]
        for index in range(N - 1, -1, -1):
            height = heights[index]
            while height < stack[-1][HEIGHT]:
                next_index, _ = stack.pop()
                prev_non_smallest[next_index] = index + 1
            stack.append((index, height))

        max_area = 0
        for left, right, height in zip(prev_non_smallest, next_non_smallest, heights):
            area = (right - left + 1) * height
            if max_area < area:
                max_area = area

        return max_area