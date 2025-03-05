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

        if n == 1:
            return 1
        return 4*(n-1) + self.coloredCells(n - 1)

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