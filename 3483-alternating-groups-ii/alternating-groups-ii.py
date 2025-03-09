class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        N = len(colors)

        res, index, streak = 0, 0, 0
        prev_color = None
        for index in range(N + k - 1):
            color = colors[index % N]
            if prev_color != color:
                # Valid case, continue the streak
                streak += 1
            else:
                # Same color, restart the streak
                streak = 1
            
            # If streak of size k, we found one valid solution, so make sure
            # to COUNT it and to set ourselves up to check whether next k-contiguous
            # tiles are also alternating :)
            if streak == k:
                streak -= 1
                res += 1

            # Loop Invariant
            prev_color = color
        
        return res
