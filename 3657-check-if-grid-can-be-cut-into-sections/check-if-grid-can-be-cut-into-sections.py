class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        # Idea: Think of this as an intervals problem (maybe). If I make VERTICAL cuts,
        # then the start_y and end_y fields DO NOT MATTER! That is, rectangles can only
        # cross vertical cuts HORIZONTALLY, so their vertical height is IRRELEVANT.
        # Similarly, start_x and end_x doesn't matter for HORIZONTAL cuts.

        # Step 1: Solve this problem for VERTICAL cuts (i.e. ignore start_y, end_y!)
        if self.solver(sorted((start_x, end_x) for start_x, start_y, end_x, end_y in rectangles)):
            return True

        # Step 2: Solve this problem for VERTICAL cuts (i.e. ignore start_y, end_y!)
        if self.solver(sorted((start_y, end_y) for start_x, start_y, end_x, end_y in rectangles)):
            return True

        # Otherwise, no solution
        return False

    def solver(self, sorted_intervals):
        valid_cuts = 0

        # Previous interval (start with first, no effect first iteration)
        prev_start, prev_end = sorted_intervals[0]

        for start, end in sorted_intervals:
            # CONDITIONS:
            # prev_start < prev_end
            # start < end
            # prev_start <= start

            # HENCE, Either:
            # (1) prev_start <= start < prev_end < end
            # (2) prev_start <= start < end < prev_end
            # (3) prev_start < prev_end <= start < end

            if start < prev_end:
                # Update prev_end to max(prev_end, end)
                if prev_end < end:
                    prev_end = end
            else:
                valid_cuts += 1
                if valid_cuts >= 2:
                    return True

                prev_start = start
                # assert prev_end < end
                prev_end = end
        
        # return valid_cuts >= 2
        return False
