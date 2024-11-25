class Solution:
    def getNextStates(self, state):
        tl, tm, tr, bl, bm, br = state
        return (
            [
                (tm, tl, tr, bl, bm, br), 
                (bl, tm, tr, tl, bm, br)
            ] if tl == 0 else
            [
                (tm, tl, tr, bl, bm, br),
                (tl, tr, tm, bl, bm, br),
                (tl, bm, tr, bl, tm, br)
            ] if tm == 0 else
            [
                (tl, tr, tm, bl, bm, br),
                (tl, tm, br, bl, bm, tr)
            ] if tr == 0 else
            [
                (bl, tm, tr, tl, bm, br),
                (tl, tm, tr, bm, bl, br)
            ] if bl == 0 else
            [
                (tl, tm, tr, bm, bl, br),
                (tl, tm, tr, bl, br, bm),
                (tl, bm, tr, bl, tm, br)
            ] if bm == 0 else
            [
                (tl, tm, br, bl, bm, tr),
                (tl, tm, tr, bl, br, bm)
            ] if br == 0 else
            [] # Should not be possible!!!
        )
        
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # top-left (tl), top-middle (tm), top-right (tr)
        # bottom-left (bl), bottom-middle (bm), bottom-right (br)
        tl, tm, tr = board[0]
        bl, bm, br = board[1]

        # UCS is essentially A* Search with a heuristic of 0. Just like
        # how DFS and BFS are the almost the exact same algorithm, with the 
        # only difference being the fringe that they use (i.e. stack for DFS
        # and queue for BFS) -- UCS is almost the exact same algorithm as DFS
        # and BFS, but uses a PRIORITY-QUEUE for its own fringe! I learned this
        # in my CSCD84 course at the University of Toronto :)
        #
        # Edit: I just realized.. UCS is pretty much useless here! Each "edge",
        # i.e. each move from one state to another have the same exact cost (i.e. 1),
        # so using a priority queue is absolutely overkill! Something like good-old
        # BFS will more than suffice here :)
        START_STATE = (tl, tm, tr, bl, bm, br)
        GOAL_STATE = (1, 2, 3, 4, 5, 0)

        # fringe is queue since using BFS!
        fringe = [(0, START_STATE)] # (cost, state)
        fringe = collections.deque(fringe)

        # fringe is heap, since using UCS!
        # fringe = [(0, START_STATE)] # (cost, state)
        visited = set()
        while len(fringe) > 0:
            cost, state = fringe.popleft()
            # cost, state = heapq.heappop(fringe)
            if state == GOAL_STATE:
                return cost
            
            if state in visited:
                continue
            visited.add(state)

            next_states = self.getNextStates(state)
            for next_state in next_states:
                fringe.append((cost + 1, next_state))
                # heapq.heappush(
                #     fringe,
                #     (cost + 1, next_state)
                # )
        
        return -1




        # DP solution attempt:
        # self.memo = {}
        # self.visited = set()
        # tl, tm, tr = board[0]
        # bl, bm, br = board[1]
        # res = self.dp(tl, tm, tr, bl, bm, br)
        # return res if res != float("inf") else -1


    
    def dp(self, tl, tm, tr, bl, bm, br):
        # Base Case: Game is solved!
        if [[tl, tm, tr], [bl, bm, br]] == [[1,2,3],[4,5,0]]:
            return 0
        
        # TODO: Might be risky to do this if in wrong order!
        if (tl, tm, tr, bl, bm, br) in self.visited:
            # return float("inf")
            return self.memo.get((tl, tm, tr, bl, bm, br), float("inf"))
        self.visited.add((tl, tm, tr, bl, bm, br))
        
        # Firstly, we need to find the 0 as that's the only one
        # that we can swap.
        # Corners only have two options, whereas middle have three!
        res = float("inf")
        if tl == 0:
            res = 1 + min(res,
                self.dp(tm, tl, tr, bl, bm, br),
                self.dp(bl, tm, tr, tl, bm, br)
            )
            # self.memo[(tl, tm, tr, bl, bm, br)] = res
            # return res
        elif tm == 0:
            res = 1 + min(res,
                self.dp(tm, tl, tr, bl, bm, br),
                self.dp(tl, tr, tm, bl, bm, br),
                self.dp(tl, bm, tr, bl, tm, br)
            )
            # self.memo[(tl, tm, tr, bl, bm, br)] = res
            # return res
        elif tr == 0:
            res = 1 + min(res,
                self.dp(tl, tr, tm, bl, bm, br),
                self.dp(tl, tm, br, bl, bm, tr)
            )
            # self.memo[(tl, tm, tr, bl, bm, br)] = res
            # return res
        elif bl == 0:
            res = 1 + min(res,
                self.dp(bl, tm, tr, tl, bm, br),
                self.dp(tl, tm, tr, bm, bl, br)
            )
            # self.memo[(tl, tm, tr, bl, bm, br)] = res
            # return res
        elif bm == 0:
            res = 1 + min(res,
                self.dp(tl, tm, tr, bm, bl, br),
                self.dp(tl, tm, tr, bl, br, bm),
                self.dp(tl, bm, tr, bl, tm, br)
            )
            # self.memo[(tl, tm, tr, bl, bm, br)] = res
            # return res
        else:
            assert br == 0
            res = 1 + min(res,
                self.dp(tl, tm, br, bl, bm, tr),
                self.dp(tl, tm, tr, bl, br, bm)
            )
            # self.memo[(tl, tm, tr, bl, bm, br)] = res
            # return res
        
        self.memo[(tl, tm, tr, bl, bm, br)] = res
        return res
        
        # raise Exception("Unreachable Code")
