class Solution:
    def getProduct(self, enumerable):
        return functools.reduce(lambda acc, x: acc * x, enumerable, 1)

    @cache
    def dp_options(self, i):
        heights = self.heights
        assert i < N

        if i == N - 1:
            return (1, heights[i])
        
        best_width, best_height = self.dp_options(i + 1)
        cur_height = heights[i]

        # Case 1: Add rectangle to current mix
        case1 = (best_width + 1, min(best_height, cur_height))
        case1_potential = (best_width + (N - i - 1)) * (min(best_height, cur_height, self.suffix_mins[i]))
        # case1_width = cur_width + 1
        # case1_height = min(cur_height, h)
        # case1_area = case1_width * case1_height

        # Case 2: Start over with current height
        case2 = (1, cur_height)
        case2_potential = (0 + (N - i)) * (min(cur_height, self.suffix_mins[i]))
        # case2_width = 1
        # case2_height = h
        # case2_area = case2_width * case2_height

        options = [self.getProduct(case1), self.getProduct(case2), case1_potential, case2_potential]
        self.res = max(self.res, max(options))
        return case2 if max(options) in [self.getProduct(case2), case2_potential] else case1
    
    @cache
    def dp2(self, i):
        heights = self.heights
        assert i < N

        if i == N - 1:
            return (1, heights[i])
        
        best_width, best_height = self.dp2(i + 1)
        cur_height = heights[i]

        # Case 1: Add rectangle to current mix
        case1 = (best_width + 1, min(best_height, cur_height))
        # case1_width = cur_width + 1
        # case1_height = min(cur_height, h)
        # case1_area = case1_width * case1_height

        # Case 2: Start over with current height
        case2 = (1, cur_height)
        # case2_width = 1
        # case2_height = h
        # case2_area = case2_width * case2_height

        return case1 if self.getProduct(case1) >= self.getProduct(case2) else case2

    @cache
    def dp_old(self, i):
        heights = self.heights
        assert i < N

        if i == N - 1:
            return (1, heights[i])
        
        best_width, best_height = self.dp(i + 1)
        cur_height = heights[i]

        # Case 1: Add rectangle to current mix
        case1 = (best_width + 1, min(best_height, cur_height))
        # case1_width = cur_width + 1
        # case1_height = min(cur_height, h)
        # case1_area = case1_width * case1_height

        # Case 2: Start over with current height
        case2 = (1, cur_height)
        # case2_width = 1
        # case2_height = h
        # case2_area = case2_width * case2_height

        return case1 if self.getProduct(case1) > self.getProduct(case2) else case2
    
    @cache
    def dp(self, i):
        # Monotonic stacks are good for finding NEXT smallest like in Daily Temperatures
        # For each index i, if we know the index of the next smallest element j (assuming there
        # is such a j, otherwise the last index), then there are two possible cases:
        #   (1) Largest area will be heights[i] * ((j-1) - i + 1), i.e. width is [i..j-1] range
        #   (2) len([i..j-1]) * heights[j] + BEST SOLUTION FROM INDEX j ONWARDS!
        N = len(self.heights)
        assert i < N
        height = self.heights[i]

        # Base Case: we are last index
        # if i == N - 1:
        #     return height
        max_area = self.suffix_min[i] * (N - i)
        index = i
        while (j := self.next_smallest[index]) != -1:
            max_area = max(max_area, (j - i) * height)
            index = j
            height = self.heights[index]
        # return max(max_area, (N - index) * height)
        return max_area
        
        j = self.next_smallest[i]

        # Base Case: No next smallest exists!
        if j == -1:
            assert height == self.suffix_min[i]
            # return self.suffix_min[i] * (N - i)
            # return height * (N - i)
            return (i, N - 1, height)
        
        assert i < j < N # assert not infinite dp loop!

        # Case (1)
        # case1 = height * (j - i)
        case1 = (i, j - 1, height)
        case1_area = height * (j - i)

        # Case (2)
        l, r, h = self.dp(j)
        # assert l == j
        print(f"{l,j=}")
        case2 = (i, r, h)
        case2_area = h * (r - i + 1)

        return case1 if case1_area >= case2_area else case2




    def largestRectangleArea(self, heights: List[int]) -> int:
        suffix_min = []
        min_height = float("inf")
        for height in reversed(heights):
            if height < min_height:
                min_height = height
            suffix_min.append(min_height)
        self.suffix_min = suffix_min[::-1]

        # Monotonic stacks are good for finding NEXT smallest like in Daily Temperatures
        # For each index i, if we know the index of the next smallest element j (assuming there
        # is such a j, otherwise the last index), then there are two possible cases:
        #   (1) Largest area will be heights[i] * ((j-1) - i + 1), i.e. width is [i..j-1] range
        #   (2) len([i..j-1]) * heights[j] + BEST SOLUTION FROM INDEX j ONWARDS!

        # For part 1 we can compute an array of next smallest index for every index i, and for
        # part 2 we can solve this DP-style to reuse same subproblems!

        # max_area = 0
        # INDEX, HEIGHT = 0, 1
        # stack = [(None, float("-inf"))] # monotonic stack
        # for index, height in enumerate(heights):
        #     i, h = None, float("-inf")
        #     while height < (stack[-1][HEIGHT]):
        #         i, h = stack.pop()
        #         max_area = max(max_area, (index - i) * height)
        #     stack.append((index, height))

        #     if i is None:
        #         continue # Nothing popped from the stack
        N = len(heights)
        INDEX, HEIGHT = 0, 1
        next_smallest = [-1] * N
        stack = [(None, float("-inf"))]
        for index, height in enumerate(heights):
            # print(f"{stack=}")
            while height < stack[-1][HEIGHT]:
                prev_index, _ = stack.pop()
                next_smallest[prev_index] = index
            stack.append((index, height))
        print(f"{stack=}")

        print(f"{next_smallest=}")

        self.next_smallest = next_smallest
        self.heights = heights

        # max_area = 0
        # for i in range(N):
        #     l, r, h = self.dp(i)
        #     max_area = max(max_area, (r - l + 1) * h)
        # return max_area
        return max(self.dp(i) for i in range(N))
    
        # return max(
        #     self.largestRectangleAreaHelper(heights),
        #     self.largestRectangleAreaHelper(heights[::-1])
        # )
        
        # prefix_min[i] = min(heights[i:])
        # prefix_min = []
        # min_height = float("inf")
        # for height in heights:
        #     if height < min_height:
        #         min_height = height
        #     prefix_min.append(min_height)
        # print(f"{prefix_min=}")
        suffix_min = []
        min_height = float("inf")
        for height in reversed(heights):
            if height < min_height:
                min_height = height
            suffix_min.append(min_height)
        suffix_min = suffix_min[::-1]
        # print(f"{suffix_min=}")


        max_area = 0
        for i in range(N):
            width, height = 1, heights[i]
            # max_area = max(max_area, width * height)
            area = width * height
            if max_area < area:
                max_area = area
            for j in range(i + 1, N):
                width += 1
                # height = min(height, heights[j])
                new_height = heights[j]
                if new_height < height:
                    height = new_height
                # max_area = max(max_area, width * height)
                area = width * height
                if max_area < area:
                    max_area = area
                # print(f"{i, j, width, height, max_area=}")
                if height == suffix_min[j]:
                    # max_area = max(max_area, (N - i) * height)
                    area = (N - i) * height
                    if max_area < area:
                        max_area = area
                    # print(f"{i, j, height=}")
                    break
        return max_area
    
    def largestRectangleAreaHelper(self, heights: List[int]) -> int:
        self.res = float("-inf")
        self.suffix_mins = []
        min_height = float("inf")
        for h in reversed(heights):
            min_height = min(min_height, h)
            self.suffix_mins.append(min_height)
        self.suffix_mins = self.suffix_mins[::-1]
        # print(f"{self.suffix_mins=}")
        self.heights = heights
        # return self.dp(0)

        res = 0
        for i in range(N):
            width, height = self.dp(i)
            res = max(res, width * height)

            width, height = self.dp2(i)
            res = max(res, width * height)

            width, height = self.dp_options(i)
            res = max(res, width * height)
        return max(res, self.res)

        # Idea: Keep track of current largest width & height combo. Always calculate
        # whatever is bigger: keeping current largest width & height combo and ADDING new
        # height to the mix, or starting over at new height.

        cur_width, cur_height = 0, 0
        res = 0
        for h in heights:
            # Case 1: Add rectangle to current mix
            case1_width = cur_width + 1
            case1_height = min(cur_height, h)
            case1_area = case1_width * case1_height

            # Case 2: Start over with current height
            case2_width = 1
            case2_height = h
            case2_area = case2_width * case2_height

            # Select maximal one
            cur_width, cur_height = (
                (case1_width, case1_height) 
                if case1_area > case2_area 
                else (case2_width, case2_height)
            )
            res = max(res, cur_width * cur_height)
        
        return res

# 1 1 1 1 1 1 1 1 1 1 5