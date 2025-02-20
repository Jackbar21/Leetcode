class Solution:
    @cache
    def dp(self, i):
        # Monotonic stacks are good for finding NEXT smallest like in Daily Temperatures
        # For each index i, if we know the index of the next smallest element j (assuming there
        # is such a j, otherwise the last index), then there are two possible cases:
        #   (1) Largest area will be heights[i] * ((j-1) - i + 1), i.e. width is [i..j-1] range
        #   (2) len([i..j-1]) * heights[j] + BEST SOLUTION FROM INDEX j ONWARDS!
        max_area = self.suffix_min[i] * (len(self.heights) - i)
        index = i
        while (j := self.next_smallest[index]) != -1:
            area = (j - i) * self.heights[index]
            if max_area < area:
                max_area = area
            index = j

        return max_area

    def largestRectangleArea(self, heights: List[int]) -> int:
        suffix_min = []
        min_height = float("inf")
        for height in reversed(heights):
            if height < min_height:
                min_height = height
            suffix_min.append(min_height)
        suffix_min = suffix_min[::-1]
        self.suffix_min = suffix_min # self.suffix_min[i] == min(heights[i:])

        N = len(heights)
        INDEX, HEIGHT = 0, 1
        next_smallest = [-1] * N
        stack = [(None, float("-inf"))]
        for index, height in enumerate(heights):
            while height < stack[-1][HEIGHT]:
                prev_index, _ = stack.pop()
                next_smallest[prev_index] = index
            stack.append((index, height))

        self.next_smallest = next_smallest
        self.heights = heights
        return max(self.dp(i) for i in range(N))
