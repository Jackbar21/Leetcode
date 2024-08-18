#               1
#       2       3       5
#     4-6-10   6-9-15. 10-15-25
#    8-12-20
#    8

# Ugly Numbers: 1 2 3 4 ... n'th ugly number
# Candidates:   5 6 10 9 15 8 12 20

# 1 2 3
# Candidates: 2,3,5 --> 3,5,4,6,10 --> 5,4,6,10,9,15

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        candidates = [1] # min heap
        ugly_nums = []
        seen = set([1])

        while len(ugly_nums) < n:
            smallest_candidate = heapq.heappop(candidates)
            ugly_nums.append(smallest_candidate)
            for new_candidate in [
                smallest_candidate * 2,
                smallest_candidate * 3,
                smallest_candidate * 5
            ]:
                if new_candidate not in seen:
                    seen.add(new_candidate)
                    heapq.heappush(candidates, new_candidate)
 
        return ugly_nums[-1]