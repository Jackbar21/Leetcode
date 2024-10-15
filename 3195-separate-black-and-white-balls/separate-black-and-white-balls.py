class Solution:
    def minimumSteps(self, s: str) -> int:
        BLACK, WHITE = '1', '0'

        # Step 1: count number of white balls, call this number NUM_WHITE_BALLS
        num_white_balls = s.count(WHITE)
        # num_black_balls = len(s) - num_white_balls

        # Idea: put leftmost white ball, to leftmost index (i.e. index == 0). 
        # Then second leftmost white ball, to second leftmost index (i.e. index == 1).
        # Keep on going until this has been done for all NUM_WHITE_BALLS white balls.
        num_seen = 0 # number of white balls seen so far
        leftmost_index = 0 # index to place next white ball to
        num_swaps = 0 # Result to return

        ball_index = 0
        while num_seen < num_white_balls:
            # assert ball_index < len(s)
            ball = s[ball_index]

            # Ball is white. Need to place it at leftmost index available, and count
            # number of swaps that would have taken.
            if ball == WHITE:
                # Number of swaps needed to get white ball to index LEFTMOST_INDEX
                num_swaps += ball_index - leftmost_index

                # Want next white ball to be at index adjacent to LEFTMOST_INDEX
                leftmost_index += 1

                # Increment number of white balls seen / taken care of so far
                num_seen += 1

            # Loop Invariant
            ball_index += 1

        return num_swaps