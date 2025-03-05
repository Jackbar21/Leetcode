class Solution:
    def coloredCells(self, n: int) -> int:
        # 1, 5, 13, 25, 41, 61, 85, 113, 145

        # 1 -> 0 == 0 * 4
        # 2 -> 4 == 1 * 4
        # 3 -> 8 == 2 * 4
        # 4 -> 12 == 3 * 4
        # 5 -> 16
        # ...

        #  n  | blocks added
        #  2  |     4
        #  3  |     8
        #  4  |     12  

        # 1 + 4*1 + 4*2 + 4*3 + 4*4 + ... + 4*(n-1)
        # == 1 + 4*(1 + 2 + 3 + 4 + ... + (n - 1))
        return 1 + 4 * (n - 1) * n // 2

        # 1 + 2 + ... + i == i * (i + 1) / 2

        # P(n): If n >= 1, then 1 + ... + n == n * (n + 1) / 2
        # PROOF (that P(n) is true):
        # Base Case: P(1)
        #   1 * (1 + 1) / 2 == 1 * (2) / 2 == 1 * 1 == 1, so True!
        # Want to show for i >= 1, if P(i) is true, then P(i + 1) is also true. Let i >= 1 be arbitrary.
        # Suppose P(i), meaning we have that 1 + ... + i == i * (i + 1) / 2 [I.H.]
        # Want to show that P(i + 1) holds, namely that 1 + ... + i + (i + 1) == (i + 1) * ((i + 1) + 1) / 2
        # 1 + ... + i + (i + 1)
        # == (1 + ... + i) + (i + 1)
        # == (i * (i + 1) / 2) + (i + 1), by [I.H.]
        # == (i^2 + i)/2 + (2i + 2)/2
        # == (i^2 + i + 2i + 2)/2
        # == (i^2 + 3i + 2)/2
        # == (i+1)*(i+2)/2, since (i+1)*(i+2) == i^2 + 2i + 1i + 2 == i^2 + 3i + 2
        # == (i + 1) * ((i + 1) + 1) / 2
        # Therefore, P(i + 1) also holds.
        #   Henceforth, by proof via induction, P(n) holds for all n >= 1.

        # if n == 1:
        #     return 1
        # return 4*(n-1) + self.coloredCells(n - 1)

        # return 1 + 4 * sum(range(1, n))
        return 1 + 4 * ((n - 1) * n) // 2

        # if n == 1:
        #     return 1
        
        # return 4 * (n - 1) + self.coloredCells(n - 1)

        # result is 1 + sum()

        # return -1
        DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        origin = (0, 0)
        queue = collections.deque([origin])
        visited = set([origin])
        while len(queue) > 0:
            x, y = queue.popleft()
            dist = abs(x) + abs(y)
            if dist >= n - 1:
                assert dist == n - 1
                continue
            # print(f"{x,y=}")
            
            for dx, dy in DIRECTIONS:
                neigh_x, neigh_y = x + dx, y + dy
                if (neigh_x, neigh_y) in visited:
                    continue
                
                visited.add((neigh_x, neigh_y))
                queue.append((neigh_x, neigh_y))
        
        return len(visited)

        # for _ in range(n - 1):
    

      #
    # T # 
  # T T T #
# T T O T T # 
  # T T T #   
    # T #     
      #             