class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        d = defaultdict(int)
        for rank in ranks:
            d[rank] += 1
        
        best_rank = min(d.keys())
        l, r = 1, best_rank * pow(cars, 2)
        while l <= r:
            mid = (l + r) // 2

            # How many cars can mechanics reapir in 'mid' minutes?
            can_repair = 0
            # It takes r * n^2 minutes to build n cars.
            # Hence, given 'mid' minutes to build cars,
            # we have that mid == r * n^2.
            # Hence, n == sqrt(mid / r)
            # ==> n^2 == time / r ==> n == sqrt(time / r)
            for rank, count in d.items():
                can_repair += count * math.floor(math.sqrt(mid / rank))
            
            if can_repair >= cars:
                # Valid solution, look for even SMALLER ones
                r = mid - 1
            else:
                l = mid + 1
        
        return l



