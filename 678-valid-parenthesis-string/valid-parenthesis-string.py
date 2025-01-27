class Solution:
    def checkValidString(self, s: str) -> bool:
        open_indices = []
        star_indices = collections.deque()
        for i, parenthese in enumerate(s):
            if parenthese == "(":
                open_indices.append(i)
                continue

            if parenthese == "*":
                star_indices.append(i)
                continue

            assert parenthese == ")"
            if len(open_indices) > 0:
                # Want to pop RIGHTMOST open parenthese!
                open_indices.pop()
                continue
            if len(star_indices) > 0:
                # Want to pop LEFTMOST stars!
                star_indices.popleft()
                continue

            # Nothing to match closed-parenthese with!
            return False

        # We now have the leftmost remaining open-parenthese indices, as well
        # as the rightmost remaining star indices. Hence, want to make sure for
        # each remaining open parenthese, that we have a star to the right of it!
        # And once we've exhausted/closed ALL remaining open parentheses, we can
        # convert all remaining stars to "" :)
        return (
            len(star_indices) >= len(open_indices) and 
            all(open_indices[-i] < star_indices[-i] for i in range(1, len(open_indices) + 1))
        )
