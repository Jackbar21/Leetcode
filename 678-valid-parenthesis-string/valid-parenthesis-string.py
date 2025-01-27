class Solution:
    def checkValidString(self, s: str) -> bool:
        open_indices = []
        star_indices = collections.deque()
        for i, parenthese in enumerate(s):
            if parenthese == "(":
                # count_open += 1
                open_indices.append(i)
                continue

            if parenthese == "*":
                # count_star += 1
                star_indices.append(i)
                continue

            assert parenthese == ")"
            if len(open_indices) > 0:
                # Want to pop RIGHTMOST open parenthese!
                # count_open -= 1 
                open_indices.pop()
                continue
            if len(star_indices) > 0:
                # count_star -= 1
                # Want to pop LEFTMOST stars!
                star_indices.popleft()
                continue

            # Nothing to match closed-parenthese with!
            return False

        # print(f"{open_indices=}")
        # print(f"{star_indices=}")
        # return len(open_indices) == 0
        while len(open_indices) > 0:
            open_index = open_indices.pop()
            # This must be to the left of a star. Hence, grab HIGHEST
            # star index for it!
            if len(star_indices) == 0:
                return False
            star_index = star_indices.pop()
            if not (open_index < star_index):
                return False
        return True