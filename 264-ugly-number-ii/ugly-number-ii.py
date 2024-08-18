#               1
#       2       3       5
#     4-6-10   6-9-15. 10-15-25
#    8-12-20
#    8

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
            
            # print(candidates)
            
        
        return ugly_nums[n - 1]





        twos, threes, fives = [1], [1], [1]

        while len(ugly_nums) < n:
            ugly_nums += [num * 2 for num in ugly_nums]
            ugly_nums += [num * 3 for num in ugly_nums]
            ugly_nums += [num * 5 for num in ugly_nums]
            
            # twos   += [num * 2 for num in ugly_nums]
            # threes += [num * 3 for num in ugly_nums]
            # fives  += [num * 5 for num in ugly_nums]
            ugly_nums = sorted(set(ugly_nums))
            # twos, threes, fives = ugly_nums.copy(), ugly_nums.copy(), ugly_nums.copy()
        
        print(twos)
        print(threes)
        print(fives)
        print(ugly_nums)
        return 1
        assert len(twos) == len(threes) == len(fives)
        assert len(twos) >= n

        ugly_nums = []
        two_ptr, three_ptr, five_ptr = 0, 0, 0

        while len(ugly_nums) < n:
            ugly_num = min(
                twos[two_ptr],
                threes[three_ptr],
                fives[five_ptr]
            )
            ugly_nums.append(ugly_num)

            # Update pointers
            while two_ptr < n and twos[two_ptr] <= ugly_num:
                two_ptr += 1
            while three_ptr < n and threes[three_ptr] <= ugly_num:
                three_ptr += 1
            while five_ptr < n and fives[five_ptr] <= ugly_num:
                five_ptr += 1

        print(ugly_nums)
        return ugly_nums[n - 1]