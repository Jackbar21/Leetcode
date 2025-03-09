class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        RED, BLUE = 0, 1
        N = len(colors)
        
        res = 0
        streak = 0 # want this to be k
        index = 0
        # opposite_color = lambda color: RED if color == BLUE else BLUE
        # prev_color = opposite_color[colors[index]]
        prev_color = None
        while index < N + k - 1:
            # # TODO: Fix this up
            # if streak == k:
            #     streak -= 1
            #     res += 1

            color = colors[index % N]
            if prev_color != color:
                # Valid case, continue the streak
                streak += 1
            else:
                # Same color, restart the streak
                streak = 1
            
            if streak == k:
                streak = k - 1
                res += 1

            # Loop Invariant
            prev_color = color
            index += 1
        
        # print(f"{streak=}")
        return res #+ (streak == k)


#          i
# [0,1,0,0,1,0,1], k = 6

# streak = 0
# index = 4
# res = 0