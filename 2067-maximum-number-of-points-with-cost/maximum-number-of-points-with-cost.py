# THIS SOLUTION is essentially copy-paste from editorial...
# I had an extremely difficult time understanding the left & right sweeps
# idea and implementing it into my own top-down dp approach. I ended giving
# up on trying to implement this idea about ~5 hours working on the problem,
# and "copied" the editorial solution (with at least understanding how it works)
# so that I can keep on going with my streak, move on, and hopefully become a better
# developer out of it :)
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        prev_row = points[0]

        for r in range(1, m):
            left_max, right_max, cur_row = [0] * n, [0] * n, [0] * n
            left_max[0], right_max[-1] = prev_row[0], prev_row[-1]

            for c in range(1, n):
                left_max[c] = max(left_max[c-1] - 1, prev_row[c])

            for c in range(n-2, -1, -1):
                right_max[c] = max(right_max[c+1] - 1, prev_row[c])
            
            for i in range(n):
                cur_row[i] = max(left_max[i], right_max[i]) + points[r][i]
            
            prev_row = cur_row
        
        return max(prev_row)
