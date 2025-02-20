class Solution:
    def dp(self, i):
        # Monotonic stacks are good for finding NEXT smallest like in Daily Temperatures
        # For each index i, if we know the index of the next smallest element j (assuming there
        # is such a j, otherwise the last index), then there are two possible cases:
        #   (1) Largest area will be heights[i] * ((j-1) - i + 1), i.e. width is [i..j-1] range
        #   (2) len([i..j-1]) * heights[j] + BEST SOLUTION FROM INDEX j ONWARDS!
        max_area = self.suffix_min[i] * (len(self.heights) - i)
        index = i
        while (j := self.next_non_smallest[index]) != -1:
            area = (j - i) * self.heights[index]
            if max_area < area:
                max_area = area
            index = j

        return max_area

    def largestRectangleArea(self, heights: List[int]) -> int:
        return self.neetcode(heights)

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
        next_non_smallest = [-1] * N
        stack = [(None, float("-inf"))]
        for index, height in enumerate(heights):
            while height < stack[-1][HEIGHT]:
                prev_index, _ = stack.pop()
                next_non_smallest[prev_index] = index
            stack.append((index, height))

        self.next_non_smallest = next_non_smallest
        self.heights = heights
        return max(self.dp(i) for i in range(N))

    def neetcode(self, heights: List[int]) -> int:
        # I read Neetcode's hints, and developed this O(N) solution from it!
        N = len(heights)
        INDEX, HEIGHT = 0, 1

        # next_non_smallest = [N - 1] * N
        # stack = [(None, float("-inf"))]
        # for index, height in enumerate(heights):
        #     while height < stack[-1][HEIGHT]:
        #         prev_index, _ = stack.pop()
        #         next_non_smallest[prev_index] = index - 1
        #     stack.append((index, height))
        
        # prev_non_smallest = [0] * N
        # stack = [(None, float("-inf"))]
        # for index in range(N - 1, -1, -1):
        #     height = heights[index]
        #     while height < stack[-1][HEIGHT]:
        #         next_index, _ = stack.pop()
        #         prev_non_smallest[next_index] = index + 1
        #     stack.append((index, height))

        # Above, but only one loop instead of two!
        next_stack, prev_stack = [(None, float("-inf"))], [(None, float("-inf"))]
        next_non_smallest = [N - 1] * N
        prev_non_smallest = [0] * N
        for i, h in enumerate(heights):
            next_index, next_height = i, h
            prev_index = N - 1 - i
            prev_height = heights[prev_index]

            while next_height < next_stack[-1][HEIGHT]:
                index, _ = next_stack.pop()
                next_non_smallest[index] = next_index - 1
            next_stack.append((next_index, next_height))

            while prev_height < prev_stack[-1][HEIGHT]:
                index, _ = prev_stack.pop()
                prev_non_smallest[index] = prev_index + 1
            prev_stack.append((prev_index, prev_height))

        max_area = 0
        for left, right, height in zip(prev_non_smallest, next_non_smallest, heights):
            area = (right - left + 1) * height
            if max_area < area:
                max_area = area

        return max_area