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
    def __init__(self):
        self.d = None
        self.num_stones = 0
    def removeStones(self, stones: List[List[int]]) -> int:
        d = {
            tuple(stone): set() for stone in stones
        }

        groups = []
        # print(sorted(stones))
        for stone in stones:
            stone_x, stone_y = stone
            group_index = -1
            for i, group in enumerate(groups):
                # if found_group:
                #     break
                # Check if stone belongs to group
                for (x, y) in group:
                    if stone_x == x or stone_y == y:
                        if group_index == -1:
                            group.add((stone_x, stone_y))
                            group_index = i
                            break
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
        
        # print(groups)
        # return 1
        res = 0
        for group in groups:
            res += len(group) - 1
        return res
                



        for i in range(len(stones)):
            x, y = stones[i]
            for stone in d:
                if stone[0] == x or stone[1] == y:
                    d[stone].add((x, y))
        
        # Remove each stone from its own list of "touching" stones
        for stone in d:
            d[stone].remove(stone)
        
        # If a stone isn't "touching" any other stone,
        # it cannot ever be removed, and hence doesn't need
        # to be considered
        # for stone in d:
        #     if d[stone] == 0:
        #         del d[stone]
        self.d = {
            key: d[key] for key in d if len(d[key]) > 0
        }

        # No stones left to remove
        if len(self.d.keys()) == 0:
            return 0

        
        # for key in self.d:
        #     print(f"{key=}: {d[key]=}")
        # return 1

        # Want to remove the stone with FEWEST number of "touching" stones.
        # Where a stone i is touch stone j if and only if stone i and j are in the
        # same row and/or i and j are in the same column.
        # next_stone = min(self.d.keys(), key=lambda k: len(self.d[k]))
        next_stone = self.nextStone()
        
        # Returns the stone that was removed, or None if no more stones can be removed
        while next_stone is not None:
            self.removeStone(next_stone)
            # next_stone = min(self.d.keys(), key=lambda k: len(self.d[k])) # O(n)
            next_stone = self.nextStone()
        

        return self.num_stones

    def nextStone(self):
        best_stone, best_val = None, float("inf")
        for stone in self.d:
            if len(self.d[stone]) > 0 and len(self.d[stone]) < best_val:
                best_val = len(self.d[stone])
                best_stone = stone
        
        return best_stone

    def removeStone(self, del_stone):
        # x, y = next_stone
        assert del_stone in self.d

        del self.d[del_stone]
        self.num_stones += 1

        for stone in self.d:
            if del_stone in self.d[stone]:
                self.d[stone].remove(del_stone)
        
        return del_stone

