# Idea 1: Just do greedy
# Idea 2: DP with connected groups
# I.e. in first case, notice:
#       {(0, 0): 2, (0, 1): 2, (1, 0): 2, (1, 2): 2, (2, 1): 2, (2, 2): 2}
# first three elements are "connected" together, as well as last 3. can use these
# as the "subproblems" for a DP solution. -- Correction, groups might not be "closed" off...
# still worth investigating this idea, but might not be as helpful as you think...


# Greedy idea 1: make sure to ALSO include non-directly touching stones for each stone in d
# Greedy idea 2: always remove stone that MINIMIZES impact, instead of one with smallest direct impact

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
                            # these two groups together. Since we
                            # can't modify groups in place, we will
                            # do this by always keeping track of a
                            # second 'new_group' list
                            # union_group = groups[group_index]
                            assert i > group_index
                            # print(f"{stone=}, groups before: {groups}")
                            # print(f"{i=}, {group_index=}, {groups[i]=}, {groups[group_index]=}")
                            # print(f"{groups[i].union(groups[group_index])=}")
                            groups[i] = groups[i].union(groups[group_index])
                            del groups[group_index]
                            # print(f"{stone=}, groups after: {groups}")
                        
                        break
                        
            
            if group_index == -1:
                # print(stone, groups)
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