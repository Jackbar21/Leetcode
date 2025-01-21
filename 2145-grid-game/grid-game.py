class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        # Idea: The fact that grid is of size 2 x n is not a coincidence. The point is that
        # player one must choose to go down EXACTLY once, and every other action will be to
        # go right. We want to find the best point in time to choose to go down, such that it
        # will minimize player 2's score.
        # Since every cell we traverse sets the value of that cell in grid to 0 (as player 1),
        # then for every index i, if player 1 chooses to go DOWN at index i, the maximum score
        # player 2 can obtain is one of the following:
        #   (1) The sum of the elements in the top row AFTER index i (i.e. grid[0][i+1:])
        #   (2) The sum of the elements in the bottom row BEFORE index i (i.e. grid[1][:i])
        # So, we need to get suffix sums for the top row, as well as prefix sums for the bottom row.
        # Then, we will be able to compute the two possible scores for player 2 at each index i, considering
        # only the maximum of the two options (since we assume player 2 plays optimally), and minimzing this
        # result.
        top_suffix = collections.deque([0]) # top_suffix[i] == sum(grid[0][i:])
        cur_sum = 0
        for num in reversed(grid[0]):
            cur_sum += num
            top_suffix.appendleft(cur_sum)
        
        bottom_prefix = [0] # bottom_prefix[i] == sum(grid[1][:i+1])
        cur_sum = 0
        for num in grid[1]:
            cur_sum += num
            bottom_prefix.append(cur_sum)
        
        min_player_2_score = float("inf")
        for i in range(len(grid[0])):
            case1 = top_suffix[i + 1]
            case2 = bottom_prefix[i]
            player_2_score = max(case1, case2)
            min_player_2_score = min(min_player_2_score, player_2_score)
        return min_player_2_score
