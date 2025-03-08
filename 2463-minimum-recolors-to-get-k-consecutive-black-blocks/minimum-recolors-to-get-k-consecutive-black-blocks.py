class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        WHITE, BLACK = "W", "B"
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

        # White blocks are at even indices, Black blocks at odd indices
        self.color_counts = color_counts
        self.k = k
        self.memo = {}
        return self.dp(0, 0)

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
        case1 = k - black_count if num_white + black_count >= k else float("inf")
        if res > case1:
            res = case1
        
        next_black_block = (self.color_counts[i + 1] if i + 1 < len(self.color_counts) else 0)

        # Case 2: Don't bother adding any balls
        # case2 = self.dp(i + 2, next_black_block)
        # if res > case2:
        #     res = case2

        # Case 3: Add balls to connect with next!
        case3 = num_white + self.dp(i + 2, black_count + num_white + next_black_block)
        if res > case3:
            res = case3

        # Case 4-N: Anything between no balls and all the balls
        # for white_count in range(1, num_white):
        for white_count in range(num_white):
            new_case = white_count + self.dp(i + 2, white_count + next_black_block)
            if res > new_case:
                res = new_case

        self.memo[(i, black_count)] = res
        return res
