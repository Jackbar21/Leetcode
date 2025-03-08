class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        WHITE, BLACK = "W", "B"


        # [0W, 5B, 1W, 5B, 99W, 8B, 99W], k = 11

        prev_color = WHITE
        color_counts = []
        cur_count = 0
        for color in blocks:
            if color == prev_color:
                cur_count += 1
                continue
            
            # Swap colors!
            color_counts.append(cur_count)
            cur_count = 1
            prev_color = color
        
        if cur_count > 0:
            color_counts.append(cur_count)
        
        # Add a white at the end of count 0
        # if len(color_counts) % 2 == 1:
        #     color_counts.append(0)
        for _ in range(3):
            color_counts.append(0)
        
        # White blocks are at even indices, Black blocks at odd indices
        print(f"{color_counts=}")

        self.color_counts = color_counts
        self.k = k
        self.memo = {}
        res = self.dp(0, 0)
        print(f"{sorted(self.memo, key = lambda k: self.memo[k])=}")
        return res

    # @cache
    def dp(self, i, black_count):
        if (i, black_count) in self.memo:
            return self.memo[(i, black_count)]

        k = self.k
        if black_count >= k:
            return 0
        
        if i >= len(self.color_counts):
            return float("inf")
        
        num_white = self.color_counts[i]
        res = float("inf")

        # Case 1: Add white balls on left to complete problem
        case1 = float("inf")
        if num_white + black_count >= k:
            case1 = k - black_count
        # for white_count in range(num_white + 1):
        #     res = min(res,
        #         self.dp(i + 2, black_count + white_count)
        #     )
        next_black_block = (self.color_counts[i + 1] if i + 1 < len(self.color_counts) else 0)

        # Case 2: Don't bother adding any balls
        case2 = self.dp(i + 2, next_black_block)

        # Case 3: Add balls to connect with next!
        case3 = num_white + self.dp(i + 2, black_count + num_white + next_black_block)

        res = min(case1, case2, case3)

        # Case 4-N: Anything between no balls and all the balls
        for white_count in range(1, num_white):
            new_case = white_count + self.dp(i + 2, white_count + next_black_block)
            res = min(res, new_case)

        self.memo[(i, black_count)] = res
        return res

        
        # If choose num_white balls, can CONNECT with next set of black balls!
        