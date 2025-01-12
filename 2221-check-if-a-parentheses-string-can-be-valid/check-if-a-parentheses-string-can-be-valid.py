class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        # Hint 1
        if len(s) % 2 == 1:
            return False
        
        locked_open = collections.deque()
        flexible = collections.deque()

        # Hint 2 -- Pass through to find all locked ')', and in doing so have number
        # of locked-open or free indices (flexible) to the left of it
        for index, parenthese in enumerate(s):
            if locked[index] == "0":
                flexible.append(index)
                continue
            
            if parenthese == "(":
                locked_open.append(index)
                continue
            
            # assert parenthese == ")"
            if len(locked_open) > 0:
                # For locked opens, we'll need to match them with something
                # on the right. So ideally, we want to match with leftmost locked-open we have!
                # So, get rid of locked-open parentheses from the RIGHT first!
                locked_open.pop()
                continue

            if len(flexible) > 0:
                flexible.popleft()
                continue

            # Cannot balance this locked closed-parenthese!
            return False 
        
        # Hint 3 -- Now, we've been able to clear ALL locked closed-parentheses,
        # we must clear out any remaining locked open-parentheses!
        if len(flexible) < len(locked_open):
            return False

        while len(locked_open) > 0:
            if locked_open.pop() >= flexible.pop():
                return False

        return True
