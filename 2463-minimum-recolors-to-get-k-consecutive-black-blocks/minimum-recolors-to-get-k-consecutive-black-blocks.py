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
        
        # Handle last consecutive blocks as well!
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
        next_black_block = (self.color_counts[i + 1] if i + 1 < len(self.color_counts) else 0)

        # Case 1: Add ALL the balls to connect with next!
        res = num_white + self.dp(i + 2, black_count + num_white + next_black_block)

        # Case 2+: Anything that is not ALL the balls (i.e. [0,N-1]).
        for white_count in range(num_white):
            new_case = white_count + self.dp(i + 2, white_count + next_black_block)
            if res > new_case:
                res = new_case

        self.memo[(i, black_count)] = res
        return res
