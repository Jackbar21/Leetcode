class Solution:
    def horizontal(self, n, rectangles):
        return False
    def vertical(self, n, rectangles):
        return False
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        # self.n = n
        # self.rectangles = rectangles
        # return self.horizontal(n, rectangles) or self.vertical(n, rectangles)

        # Idea: Think of this as an intervals problem (maybe). If I make VERTICAL cuts,
        # then the start_y and end_y fields DO NOT MATTER! That is, rectangles can only
        # cross vertical cuts HORIZONTALLY, so their vertical height is IRRELEVANT.
        # Similarly, start_x and end_x doesn't matter for HORIZONTAL cuts.

        def solver(intervals):
            intervals.sort()

            valid_cuts = 0

            # Last interval
            prev_start, prev_end = intervals[0]

            for i in range(1, len(intervals)):
                start, end = intervals[i]

                assert prev_start <= start

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
                    # non_problematic_intervals.add((prev_end, start))
                    # valid_cuts += start - prev_end + 1
                    valid_cuts += 1
                    if valid_cuts >= 2:
                        return True

                    prev_start = start
                    # assert prev_end < end
                    prev_end = end
            
            # print(f"{non_problematic_intervals=}")
            return valid_cuts >= 2



        def solver_linesweep(intervals):
            # print(f"{list(intervals)=}")
            line_sweep = defaultdict(int)
            for start, end in intervals:
                # Now, it is fine to cut at start. It is also fine to cut at end
                # it is just NOT fine however, to cut at any x such that start < x < end
                if start + 1 < end:
                    line_sweep[start + 1] += 1
                    line_sweep[end] -= 1
            
            prev_axis = 0
            active_intervals = 0
            good_intervals = []
            count = 0
            left = False
            right = False
            for axis in sorted(line_sweep.keys()):
                if prev_axis < axis and active_intervals == 0:
                    # good_intervals.append((prev_axis, axis - 1))
                    count += axis - prev_axis
                    # count -= prev_axis == 0
                    left = left or (prev_axis == 0)
                    right = right or (axis == n)
                    # count -= axis == n
                    if count >= 2:
                        return True
                    prev_axis = axis
                
                active_intervals += line_sweep[axis]
            
            if prev_axis < n - 1:
                good_intervals.append((prev_axis, n - 2))
            print(f"{active_intervals=}, {prev_axis=}, {n=}, {good_intervals=}")
            # count += n - prev_axis - 2
            print(f"{count=}, {left=}, {right=}")
            return count >= 2
            return sum(r - l + 1 for l, r in good_intervals) >= 2

        # Step 1: Solve this problem for VERTICAL cuts (i.e. ignore start_y, end_y!)
        if solver([(start_x, end_x) for start_x, start_y, end_x, end_y in rectangles]):
            return True
        # Step 2: Solve this problem for VERTICAL cuts (i.e. ignore start_y, end_y!)
        if solver([(start_y, end_y) for start_x, start_y, end_x, end_y in rectangles]):
            return True
        # Otherwise, no solution
        return False

        line_sweep = defaultdict(int)
        for start_x, start_y, end_x, end_y in rectangles:
            # Ignore start_y, end_y
            start, end = start_x, end_x

            # Now, it is fine to cut at start. It is also fine to cut at end
            # it is just NOT fine however, to cut at any x such that start < x < end
            if start + 1 < end - 1:
                line_sweep[start + 1] += 1
                line_sweep[end] -= 1
        
        print(f"problematic_positions={len(line_sweep)}, possible_positions={n-2}")
        # if len(line_sweep) == n - 1:
        #     return True
        
        non_overlap_count = 0
        active_intervals = 0 # Number of overlapping rectangles at current x position
        prev_pos = 0
        line_sweep = {key: line_sweep[key] for key in sorted(line_sweep.keys())}
        #print(f"{line_sweep=}")
        for x_axis in sorted(line_sweep.keys()):
            # if x_axis in [0, n]:
            #     continue
            if prev_pos < x_axis and active_intervals == 0:
                non_overlap_count += 1
            prev_pos = x_axis
            active_intervals += line_sweep[x_axis]
            # non_overlap_count += (active_intervals == 0)
            if non_overlap_count == 2:
                return True
        
        # if prev_pos < x_axis and active_intervals == 0:
        #     non_overlap_count += 1
        # prev_pos = x_axis
        # if non_overlap_count == 2:
        #     return True
        
        assert non_overlap_count < 2 # TODO: Otherwise, return!
        #print(f"{non_overlap_count=}, {active_intervals=}")

        # Step 2: No solution for VERTICAL cuts, so check for HORIZONTAL cuts (i.e. ignore start_x, end_x!)
        line_sweep = defaultdict(int)
        for start_x, start_y, end_x, end_y in rectangles:
            # Ignore start_x, end_x!
            start, end = start_y, end_y
            # line_sweep[start + 1] += 1
            # line_sweep[end] -= 1 

            # Now, it is fine to cut at start. It is also fine to cut at end
            # it is just NOT fine however, to cut at any x such that start < x < end
            if start + 1 < end - 1:
                line_sweep[start + 1] += 1
                line_sweep[end] -= 1
        
        print(f"problematic_positions={len(line_sweep)}, possible_positions={n-2}")
        # if len(line_sweep) == n - 1:
        #     return True

        
        non_overlap_count = 0
        active_intervals = 0 # Number of overlapping rectangles at current x position
        prev_pos = 0
        line_sweep = {key: line_sweep[key] for key in sorted(line_sweep.keys())}
        #print(f"{line_sweep=}")
        for y_axis in sorted(line_sweep.keys()):
            # if y_axis in [0, n]:
            #     continue
            if prev_pos < y_axis and active_intervals == 0:
                non_overlap_count += 1
            prev_pos = y_axis
            active_intervals += line_sweep[y_axis]
            # non_overlap_count += (active_intervals == 0)
            if non_overlap_count == 2:
                return True
        
        # if prev_pos < y_axis and active_intervals == 0:
        #     non_overlap_count += 1
        # prev_pos = y_axis
        # if non_overlap_count == 2:
        #     return True
        
        assert non_overlap_count < 2 # TODO: Otherwise, return!
        #print(f"{non_overlap_count=}, {active_intervals=}")
        return False