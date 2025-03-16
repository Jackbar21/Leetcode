class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        d = defaultdict(int)
        for rank in ranks:
            d[rank] += 1

        best_rank = min(ranks)
        l, r = 1, best_rank * pow(cars, 2)
        while l <= r:
            mid = (l + r) // 2

            # How many cars can mechanics reapir in 'mid' minutes?
            # For a mechanic with a rank of r, it takes r * n^2 minutes to build n cars.
            # Hence, given 'mid' minutes to build cars, we have that: 
            #       mid == r * n^2
            #       ==> r * n^2 == mid
            #       ==> n^2 == mid / r
            #       ==> n == sqrt(mid / r)
            can_repair = 0
            for rank, count in d.items():
                can_repair += count * math.floor(math.sqrt(mid / rank))

            if can_repair >= cars:
                # Valid solution, look for even SMALLER ones
                r = mid - 1
            else:
                # Invalid solution, look for larger (worse) but VALID ones
                l = mid + 1
        
        return l
