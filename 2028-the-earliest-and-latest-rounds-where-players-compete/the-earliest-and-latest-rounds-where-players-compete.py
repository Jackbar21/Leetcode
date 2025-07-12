class Solution:
    ### EDITORIAL: ###
    def earliestAndLatest(
        self, n: int, firstPlayer: int, secondPlayer: int
    ) -> List[int]:
        @cache
        def dp(n: int, f: int, s: int) -> (int, int):
            if f + s == n + 1:
                return (1, 1)

            # F(n,f,s)=F(n,n+1-s,n+1-f)
            if f + s > n + 1:
                return dp(n, n + 1 - s, n + 1 - f)

            earliest, latest = float("inf"), float("-inf")
            n_half = (n + 1) // 2

            if s <= n_half:
                # s On the left or in the middle
                for i in range(f):
                    for j in range(s - f):
                        x, y = dp(n_half, i + 1, i + j + 2)
                        earliest = min(earliest, x)
                        latest = max(latest, y)
            else:
                # s on the right
                # s'
                s_prime = n + 1 - s
                mid = (n - 2 * s_prime + 1) // 2
                for i in range(f):
                    for j in range(s_prime - f):
                        x, y = dp(n_half, i + 1, i + j + mid + 2)
                        earliest = min(earliest, x)
                        latest = max(latest, y)

            return (earliest + 1, latest + 1)

        # F(n,f,s) = F(n,s,f)
        if firstPlayer > secondPlayer:
            firstPlayer, secondPlayer = secondPlayer, firstPlayer

        earliest, latest = dp(n, firstPlayer, secondPlayer)
        dp.cache_clear()
        return [earliest, latest]
    ### MY ATTEMPT: ###
    """
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        # return [
        #     self.minSolver(n, firstPlayer, secondPlayer),
        #     self.maxSolver(n, firstPlayer, secondPlayer)
        # ]

        # num_rounds = 0
        # while len(arr) >= 2:
        #     num_rounds += 1

        #     new_arr = [None] * len(arr)
        self.first, self.second = firstPlayer, secondPlayer
        self.memo = {}

        print(f"{self.dp(range(1, n + 1))=}")
    
    # Max rounds
    @cache
    def dp(self, arr):
        key = tuple(arr)
        if key in self.memo:
            return self.memo[key]
        
        if sorted([arr[0], arr[-1]]) == sorted([self.first, self.second]):
            return 1
        
        if len(arr) == 2:
            assert self.first in arr
            assert self.second in arr
            return 1
        
        case1 = 1 + self.dp(arr[1:]) if arr[0] not in [self.first, self.second] else -1
        case2 = 1 + self.dp(arr[:len(arr)-1]) if arr[-1] not in [self.first, self.second] else -1
        res = max(case1, case2)
        self.memo[key] = res
        return res


    
    def minSolver(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        arr = collections.deque(range(1, n + 1))
        count = 0
        while len(arr) > 2:
            first_index = arr.index(firstPlayer)
            second_index = arr.index(secondPlayer)
            min_index = min(first_index, second_index)
            max_index = max(first_index, second_index)

            count += 1
            new_arr = [None] * len(arr)
            if len(arr) % 2 == 1:
                new_arr[len(arr) // 2] = arr[len(arr) // 2]
            # new_arr = collections.deque()
            l, r = -1, len(arr)
            for _ in range(len(arr) // 2):
                l += 1
                r -= 1
                left = arr.popleft()
                right = arr.pop()
                if left in [firstPlayer, secondPlayer] and right in [firstPlayer, secondPlayer]:
                    print(f"{count=}")
                    count -= 1
                    break
                elif left in [firstPlayer, secondPlayer]:
                    # new_arr.appendleft(left)
                    new_arr[l] = left
                elif right in [firstPlayer, secondPlayer]:
                    # new_arr.append(right)
                    new_arr[r] = right
                else:
                    # we want first & second player to fight as early as possible,
                    # meaning we want winner to be left of min_index or right of max_index
                    if not (r > max_index):
                        new_arr[l] = left
                    else:
                        new_arr[r] = right
                
            print(f"{new_arr=}")
            new_arr = [el for el in new_arr if el is not None]
            arr = collections.deque(new_arr)
            print(f"{new_arr=}")
            print()

        count += 1
        print(f"{arr=}, {first_index=}, {second_index=}")
        return count
    
    def maxSolver(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        arr = collections.deque(range(1, n + 1))
        # print(f"{arr=}")
        count = 0
        while len(arr) > 2:
            print(f"{count=}")
            first_index = arr.index(firstPlayer)
            second_index = arr.index(secondPlayer)
            min_index = min(first_index, second_index)
            max_index = max(first_index, second_index)

            count += 1
            new_arr = [None] * len(arr)
            if len(arr) % 2 == 1:
                new_arr[len(arr) // 2] = arr[len(arr) // 2]
            # new_arr = collections.deque()
            l, r = -1, len(arr)
            for _ in range(len(arr) // 2):
                l += 1
                r -= 1
                left = arr.popleft()
                right = arr.pop()
                if left in [firstPlayer, secondPlayer] and right in [firstPlayer, secondPlayer]:
                    print(f"{count=}")
                    count -= 1
                    break
                elif left in [firstPlayer, secondPlayer]:
                    # new_arr.appendleft(left)
                    new_arr[l] = left
                elif right in [firstPlayer, secondPlayer]:
                    # new_arr.append(right)
                    new_arr[r] = right
                else:
                    # we want first & second player to fight as late as possible,
                    # meaning we want winner to be between min_index and max_index
                    if r < max_index:
                        new_arr[r] = right
                    else:
                        new_arr[l] = left
                
            # print(f"{new_arr=}")
            new_arr = [el for el in new_arr if el is not None]
            arr = collections.deque(new_arr)
            # print(f"{new_arr=}")
            # print()

        count += 1
        # print(f"{arr=}, {first_index=}, {second_index=}")
        return count
    """