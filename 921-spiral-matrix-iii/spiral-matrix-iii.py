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
        # print(f"FASASA: {self.visited_arr}")
        return len(self.visited) >= self.rows * self.cols
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
            # print("1 END STATE REACHED!!!")
            # print(r, c)
            return

        self.visited.add((r, c))
        self.visited_arr.append((r, c))

        if self.isEndState():
            # print("other end state reached")
            return
        
        # If I can go right, go right!
        right_direction = self.getTurnRightDirection(cur_direction)
        # print(r,c)
        # print(f"{right_direction=}")
        right_r, right_c = self.getNext(r, c, right_direction)
        # print(right_r, right_c)
        if self.isValid(right_r, right_c):
            # self.visited.add((right_r, right_c))
            # self.visited_arr.append((right_r, right_c))
            if self.isEndState():
                return
            self.gone_right += 1
            return self.spiralMatrixHelper(right_r, right_c, right_direction)

        # If I can go forward, go forward!
        forw_r, forw_c = self.getNext(r, c, cur_direction)
        if self.isValid(forw_r, forw_c):
            # self.visited.add((forw_r, forw_c))
            # self.visited_arr.append((forw_r, forw_c))
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
        
        # incrementing rows goes southward (downwards)
        # incrementing cols goes eastward (rightwards)

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
        # self.count += 1
        # assert self.count <= 5

        # Only call this function if you are NOT in an end state
        assert not self.isEndState()

        # print(f"URGENT: {r=}, {c=}, {self.rows=}, {self.cols=}")
        assert 0 <= r < self.rows and 0 <= c < self.cols
        
        # Assert we are currently somewhere on border of matrix
        assert r == 0 or r == self.rows - 1 or c == 0 or c == self.cols - 1

        original_r, original_c = r, c
        # i = 0
        # print(f"{original_r=}, {original_c}")
        while not self.isValid(r, c):
            r, c = self.getNextOnBorder(r, c)
            # print(f"BORDER HOP: {r}, {c}")
            # i += 1
            # assert i < 10
        
        assert self.isValid(r, c)
        return (r, c)

        # bounce_direction = self.getTurnRightDirection(cur_direction)
        # assert bounce_direction in ["north", "east", "south", "west"]

        # # Assert we are currently somewhere on border of matrix
        # # print(f"findNextAvailable: {r=}, {c=}, {bounce_direction=}")
        # assert r == 0 or r == self.rows - 1 or c == 0 or c == self.cols - 1
        # orig_r, orig_c = r, c
        # while not self.isValid(r, c):
        #     r, c = self.getNext(r, c, bounce_direction)
        #     assert r != orig_r or c != orig_c
        #     if self.shouldChangeBounceDirection(bounce_direction, (r, c)):
        #         direction = self.getTurnRightDirection(bounce_direction)
        #         return self.findNextAvailable(r, c, direction)

        # return (r, c)
        # raise Exception("UNREACHABLE CODE")

        # if bounce_direction == "south":
        #     while not self.isValid(next_r, next_c):
        #         next_r, next_c = self.getNext(r, c, bounce_direction)
        #         if next_r == self.rows - 1:
        #             direction = self.getTurnRightDirection(bounce_direction)
        #             return self.findNextAvailable(next_r, next_c, direction)
        

        # while not self.isValid(next_r, next_c):
        #     if bounce_direction == "south":
        #         next_r, next_c = self.getNext(r, c, bounce_direction)

        # for i in range(self.rows):
        #     next_r, next_c = (i, self.cols - 1)
        #     # print(next_r, next_c, self.isValid(next_r, next_c))
        #     if self.isValid(next_r, next_c):
        #         return (next_r, next_c)
        
        # for i in range(self.cols - 1, -1, -1):
        #     next_r, next_c = (self.rows - 1, i)
        #     # print(next_r, next_c, self.isValid(next_r, next_c))
        #     if self.isValid(next_r, next_c):
        #         return (next_r, next_c)
        
        # # raise Exception("No next element found")
        # return (4,5)

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
        
        # If not start on border, call algorithm normally
        # if not (r == 0 or r == self.rows - 1 or c == 0 or c == self.cols - 1):
        #     self.spiralMatrixHelper(rStart, cStart, "north")
        #     return self.visited_arr

        
        if r == self.rows - 1 and c != self.cols - 1:
            assert r > 0 # True since self.rows > 1
            self.visited.add((rStart, cStart))
            self.visited.add((rStart, cStart + 1))
            self.visited_arr.append((rStart, cStart))
            self.visited_arr.append((rStart, cStart + 1))
            if c == 0:
                self.spiralMatrixHelper(rStart - 1, cStart, "north")
            elif c < self.cols - 1:
                self.spiralMatrixHelper(rStart, cStart - 1, "west")
            return self.visited_arr
        
        if c == self.cols - 1 and r > 0:
            self.visited.add((rStart, cStart))
            self.visited_arr.append((rStart, cStart))
            # if self.cols == 1 or c == 0:
            #     # Single column case
            #     assert self.cols == 1 and c == 0
            #     # print("TRUE BROOO")
            #     # print(rStart, cStart)
            #     # want below, but if not exist: get above
            #     if self.isValid(rStart + 1, cStart):
            #         self.spiralMatrixHelper(rStart + 1, cStart, "west")
            #     else:
            #         assert self.isValid(rStart - 1, cStart)
            #         self.spiralMatrixHelper(rStart - 1, cStart, "east")
            #     return self.visited_arr

            if r == self.rows - 1:
                self.spiralMatrixHelper(rStart, cStart - 1, "west")
            else:
                self.spiralMatrixHelper(rStart + 1, cStart, "south")
            return self.visited_arr

        # Terminate
        self.spiralMatrixHelper(rStart, cStart, "north")
        return self.visited_arr



#         self.spiralMatrixHelper(rStart, cStart, "north")
#         return visited_arr

#         # Handle starting at corner cases if needed
#         # Bottom-left corner case (south-west)
#         # print(f"{rStart=}, {rows=}, {cStart=}, {cols=}")
#         if rStart == rows - 1 and cStart == 0 and rows > 1 and cols > 1:
#             for (r, c) in [
#                 (rStart, cStart),
#                 (rStart, cStart + 1)
#             ]:
#                 self.visited.add((r, c))
#                 self.visited_arr.append((r, c))
#             # print(f"RSSJADK: {rStart=}, {cStart=}" )
#             self.spiralMatrixHelper(rStart - 1, cStart, "north")
#             return self.visited_arr
        
#         if rStart == rows - 1 and cStart == cols - 1 and rows > 1 and cols > 1:
#             for (r, c) in [
#                 (rStart, cStart),
#                 # (rStart, cStart - 1)
#             ]:
#                 self.visited.add((r, c))
#                 self.visited_arr.append((r, c))
#             self.spiralMatrixHelper(rStart, cStart - 1, "west")
#             return self.visited_arr

#         self.spiralMatrixHelper(rStart, cStart, "north")
#         return self.visited_arr



# # 1 2 3 4
# # 5 6 7 8
# # A B C D
# # E F G H

# 1
# 2

# 1 2 3 4 5 6
# A B C D E F
# G H I J K L
# M N O P Q R
# S T U V W X

# 1 2 3 4 5 6 7
# A B C D E F G
# H I J K L M N