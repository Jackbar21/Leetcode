class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # Check same number of "L" and "R"s first!
        start_count = len(start) - start.count("_")
        target_count = len(target) - target.count("_")
        if start_count != target_count:
            return False
        
        # No letters to move!
        if start_count == target_count == 0:
            return True

        l, r = 0, len(start) - 1
        i, j = 0, len(target) - 1
        while i <= j:
            if l > r:
                return False
            
            if start[l] == "_":
                l += 1
                continue
            if start[r] == "_":
                r -= 1
                continue
            if target[i] == "_":
                i += 1
                continue
            if target[j] == "_":
                j -= 1
                continue
            
            s, t = start[l], target[i]
            if s == t and ((s == "L" and l >= i) or (s == "R" and l <= i)):
                l += 1
                i += 1
                continue
            
            s, t = start[r], target[j]
            if s == t and ((s == "L" and r >= j) or (s == "R" and r <= j)):
                r -= 1
                j -= 1
                continue
            
            # Permanently stuck!
            return False

        return True

        available = collections.deque((i, char) for i, char in enumerate(start) if char != "_")
        need = collections.deque((i, char) for i, char in enumerate(target) if char != "_")
        if len(available) != len(need):
            return False

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
