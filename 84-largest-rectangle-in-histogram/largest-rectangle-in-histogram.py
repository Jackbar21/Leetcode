class Solution:
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
    
    def neetcode(self, heights: List[int]) -> int:
        # print(f"{heights=}")
        N = len(heights)
        INDEX, HEIGHT = 0, 1

        next_smallest = [-1] * N
        stack = [(None, float("-inf"))]
        for index, height in enumerate(heights):
            while height < stack[-1][HEIGHT]:
                prev_index, _ = stack.pop()
                next_smallest[prev_index] = index
            stack.append((index, height))
        
        prev_smallest = [-1] * N
        stack = [(None, float("-inf"))]
        for index in range(N - 1, -1, -1):
            height = heights[index]
            # print(f"{stack=}, {index=}, {height=}")
            while height < stack[-1][HEIGHT]:
                next_index, _ = stack.pop()
                prev_smallest[next_index] = index
            stack.append((index, height))
        # prev_smallest = prev_smallest[::-1]
        
        # print(f"{next_smallest=}")
        # print(f"{prev_smallest=}")

        max_area = 0
        for index, height in enumerate(heights):
            left = prev_smallest[index] + 1 if prev_smallest[index] != -1 else 0
            right = next_smallest[index] - 1 if next_smallest[index] != -1 else N - 1
            area = (right - left + 1) * height
            if max_area < area:
                max_area = area

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
