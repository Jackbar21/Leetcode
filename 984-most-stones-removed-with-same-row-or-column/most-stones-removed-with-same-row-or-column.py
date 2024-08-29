class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        groups = [] # List of lists of "touching" stones.
        for stone in stones:
            stone_x, stone_y = stone
            group_index = -1
            for i, group in enumerate(groups):
                # Check if stone belongs to group
                for (x, y) in group:
                    if stone_x == x or stone_y == y:
                        if group_index == -1:
                            group.add((stone_x, stone_y))
                            group_index = i
                        else:
                            # We've already found a group.
                            # Since we can add the stone to this
                            # other group as well, we should MERGE
                            # these two groups together.
                            assert i > group_index
                            groups[i] = groups[i].union(groups[group_index])
                            del groups[group_index]
                        
                        break
                        
            if group_index == -1:
                groups.append(set([(stone_x, stone_y)]))

        # Idea: if we can find a connected network of stones such
        # that they all "touch" each other. A stone X directly touches 
        # a stone Y if and only if stone X and stone Y are in the same 
        # row and/or column. A stone X' and stone Y' "touch" each other if:
        #  (1) stone X' and stone Y' directly touch one another, OR
        #  (2) there exists a sequence of stones S_1,S_2,...,S_n such that 
        #      stone X' touches stone S_1, stone S_{i} touches stone S_{i+1}
        #      for all 1 <= i < n, and stone S_n touches stone Y'
        res = 0
        for group in groups:
            num_stones = len(group)
            # In a group of 'num_stones' stones, we can remove
            # num_stones - 1 many stones, and then be left with
            # exactly 1 stone (which we than can't delete since it
            # doesn't touch any other stone, let alone directly touch one).
            res += num_stones - 1
        return res