class Solution:
    def canChange(self, start: str, target: str) -> bool:
        available = collections.deque((i, char) for i, char in enumerate(start) if char != "_")
        need = collections.deque((i, char) for i, char in enumerate(target) if char != "_")
        # assert len(start) == len(target)
        # n = len(start)
        if len(available) != len(need):
            return False

        # for i in range(n):
        #     if start[i] == target[i]:
        #         continue
        # # print(f"{available=}")
        # # print(f"{need=}")

        INDEX, PIECE = 0, 1
        while len(need) > 0:
            # See if can pop from left / right each time,
            # and at any point if stuck, then no solution!
            need_index, need_piece = need[0]
            index, piece = available[0]
            if (
                (piece == need_piece == "R" and index <= need_index) # Move Right!
                or (piece == need_piece == "L" and need_index <= index) # Move Left!
            ):
                available.popleft()
                need.popleft()
                continue
            
            need_index, need_piece = need[-1]
            index, piece = available[-1]
            if (
                (piece == need_piece == "R" and index <= need_index) # Move Right!
                or (piece == need_piece == "L" and need_index <= index) # Move Left!
            ):
                available.pop()
                need.pop()
                continue
            
            return False

            
        return True
    
    
