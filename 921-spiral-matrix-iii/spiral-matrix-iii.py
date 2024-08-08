class Solution:
    def __init__(self):
        self.rows = None
        self.cols = None
        self.visited = set()
        self.visited_arr = []
        self.gone_right = 0
        self.gone_forward = 0
    def isEndState(self):
        assert len(self.visited) <= self.rows * self.cols
        return len(self.visited) == self.rows * self.cols
    def getNext(self, x, y, direction):
        # incrementing rows goes southward (downwards)
        # incrementing cols goes eastward (rightwards)
        if direction == "down" or direction == "south":
            return (x + 1, y)
        
        if direction == "up" or direction == "north":
            return (x - 1, y)
        
        if direction == "left" or direction == "west":
            return (x, y - 1)

        if direction == "right" or direction == "east":
            return (x, y + 1)
        
        # Unreachable code
        raise Exception("Invalid direction")

    def isOutOfBounds(self, x, y):
        return (
            x < 0
            or x >= self.rows
            or y < 0
            or y >= self.cols
        )
    def isValid(self, x, y):
        return not self.isOutOfBounds(x, y) and (x, y) not in self.visited
    def getTurnRightDirection(self, direction):
        d = {
            "north": "east",
            "east": "south",
            "south": "west",
            "west": "north"
        }
        assert direction in d
        return d[direction]
    def spiralMatrixHelper(self, r, c, cur_direction):
        if (r, c) in self.visited:
            return

        self.visited.add((r, c))
        self.visited_arr.append((r, c))

        if self.isEndState():
            return
        
        # If I can go right, go right!
        right_direction = self.getTurnRightDirection(cur_direction)
        right_r, right_c = self.getNext(r, c, right_direction)
        if self.isValid(right_r, right_c):
            if self.isEndState():
                return
            self.gone_right += 1
            return self.spiralMatrixHelper(right_r, right_c, right_direction)

        # If I can go forward, go forward!
        forw_r, forw_c = self.getNext(r, c, cur_direction)
        if self.isValid(forw_r, forw_c):
            if self.isEndState():
                return
            self.gone_forward += 1
            return self.spiralMatrixHelper(forw_r, forw_c, cur_direction)
        
        # If I can't go right, and I can't go forward:
            # return if visited every element
            # else do "loopedy-loop" to get next element to see
        assert not self.isEndState()
        next_r, next_c = self.findNextAvailable(r, c, cur_direction)
        assert self.isValid(next_r, next_c)
        new_direction = (
            "south" if next_r == 0 else
            "north" if next_r == self.rows - 1 else
            "east" if next_c == 0 else
            "west" if next_c == self.cols - 1
            else ""
        )
        assert new_direction != ""
        return self.spiralMatrixHelper(next_r, next_c, new_direction)

    def getNextOnBorder(self, r, c):
        # First, handle all four corners
        if r == 0 and c == 0:
            return (r, c + 1)
        if r == 0 and c == self.cols - 1:
            return (r + 1, c)
        if r == self.rows - 1 and c == 0:
            return (r - 1, c)
        if r == self.rows - 1 and c == self.cols - 1:
            return (r, c - 1)

        # Otherwise, only four possible cases:
        if r == 0:
            return (r, c + 1)
        
        if r == self.rows - 1:
            return (r, c - 1)
        
        if c == 0:
            return (r - 1, c)
        
        assert c == self.cols - 1
        return (r + 1, c)

    def findNextAvailable(self, r, c, cur_direction):
        # Only call this function if you are NOT in an end state
        assert not self.isEndState()
        assert 0 <= r < self.rows and 0 <= c < self.cols
        
        # Assert we are currently somewhere on border of matrix
        assert r == 0 or r == self.rows - 1 or c == 0 or c == self.cols - 1

        original_r, original_c = r, c
        while not self.isValid(r, c):
            r, c = self.getNextOnBorder(r, c)
        
        assert self.isValid(r, c)
        return (r, c)

    def shouldChangeBounceDirection(self, direction, pos):
            r, c = pos
            return ((direction == "south" and r == self.rows - 1)
                or (direction == "north" and r == 0)
                or (direction == "east" and c == self.cols - 1)
                or (direction == "west" and c == 0)
            )

    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        self.rows, self.cols = rows, cols
        self.count = 0
        r, c = rStart, cStart

        # Handle cases when rows == 1 or cols == 1 manually
        if rows == 1 and cols == 1:
            return [(0,0)]
        elif rows == 1:
            is_right_next = True
            leftmost, rightmost = cStart, cStart
            res = [(rStart, cStart)]
            assert rStart == 0
            while len(res) < self.cols:
                if is_right_next:
                    rightmost += 1
                    val = rightmost
                    if rightmost >= self.cols:
                        leftmost -= 1
                        val = leftmost
                    res.append((rStart, val))
                else:
                    leftmost -= 1
                    val = leftmost
                    if leftmost < 0:
                        rightmost += 1
                        val = rightmost
                    # val = leftmost if leftmost > 0 else rightmost
                    res.append((rStart, val))
                # Loop Invariant
                is_right_next = not is_right_next

            return res
        elif cols == 1:
            is_south_next = True
            southmost, northmost = rStart, rStart
            res = [(rStart, cStart)]
            assert cStart == 0
            while len(res) < self.rows:
                if is_south_next:
                    southmost += 1
                    val = southmost
                    if southmost >= self.rows:
                        northmost -= 1
                        val = northmost
                    res.append((val, cStart))
                else:
                    northmost -= 1
                    val = northmost
                    if northmost < 0:
                        southmost += 1
                        val = southmost
                    # val = leftmost if leftmost > 0 else rightmost
                    res.append((val, cStart))
                # Loop Invariant
                is_south_next = not is_south_next

            return res

        assert rows > 1 and cols > 1
        if r == self.rows - 1 and c != self.cols - 1:
            assert r > 0 # True since self.rows > 1
            self.visited.add((rStart, cStart))
            self.visited.add((rStart, cStart + 1))
            self.visited_arr.append((rStart, cStart))
            self.visited_arr.append((rStart, cStart + 1))

            if c == 0:
                self.spiralMatrixHelper(rStart - 1, cStart, "north")
            else:
                self.spiralMatrixHelper(rStart, cStart - 1, "west")

            return self.visited_arr
        
        if c == self.cols - 1 and r > 0:
            self.visited.add((rStart, cStart))
            self.visited_arr.append((rStart, cStart))

            if r == self.rows - 1:
                self.spiralMatrixHelper(rStart, cStart - 1, "west")
            else:
                self.spiralMatrixHelper(rStart + 1, cStart, "south")

            return self.visited_arr

        self.spiralMatrixHelper(rStart, cStart, "north")
        return self.visited_arr