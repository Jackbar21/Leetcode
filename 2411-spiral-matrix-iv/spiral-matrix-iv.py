# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=ROW, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.m = None
        self.n = None
        self.head = None
        self.matrix = None
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        self.m, self.n = m, n
        self.head = head
        self.matrix = [[-1] * self.n for _ in range(self.m)]


        # Get initial corners
        top_left = (0,0)
        top_right = (0, self.n - 1)
        bottom_left = (self.m - 1, 0)
        bottom_right = (self.m - 1, self.n - 1)

        # return []

        corners = [top_left, top_right, bottom_left, bottom_right]
        return self.populateBorder(corners)

    
    def populateBorder(self, corners):
        ROW, COL = 0, 1
        assert len(corners) == 4
        top_left, top_right, bottom_left, bottom_right = corners
        # print(f"TOP: {top_left=}, {top_right=}, {bottom_left=}, {bottom_right=}")
        # # print(self.head)
        # print(self.matrix)
        # tl, tr, bl, br = corners

        assert top_left[ROW] == top_right[ROW]
        assert bottom_left[ROW] == bottom_right[ROW]
        assert top_left[COL] == bottom_left[COL]
        assert top_right[COL] == bottom_right[COL]

        assert top_left[ROW] <= bottom_left[ROW]
        assert top_left[COL] <= top_right[COL]
        assert top_right[ROW] <= bottom_right[ROW]
        # assert top_right[COL] >= top_left[COL]
        # assert bottom_left[ROW] >= top_left[ROW]
        assert bottom_left[COL] <= bottom_right[COL]
        # assert bottom_right[ROW] >= top_right[ROW]
        # assert bottom_right[COL] >= bottom_left[COL]

        # Case 1: One row and one column
        if top_left == bottom_left == bottom_right == top_right:
            # print("CASE 1")
            if not self.head:
                return self.matrix
            x, y = top_left
            self.matrix[x][y] = self.head.val
            assert self.head.next is None
            return self.matrix
        
        # Case 2: One row
        elif (top_left[ROW] == bottom_left[ROW]) or (top_right[ROW] == bottom_right[ROW]):
            # print("CASE 2")
            assert (top_left[ROW] == bottom_left[ROW]) and (top_right[ROW] == bottom_right[ROW])
            # Just one row, so go from top_left to top_right, until done
            x = top_left[ROW]
            for y in range(top_left[COL], top_right[COL] + 1):
                if not self.head:
                    return self.matrix
                self.matrix[x][y] = self.head.val
                self.head = self.head.next

        # Case 3: One column
        elif (top_left[COL] == top_right[COL]) or (bottom_left[COL] == bottom_right[COL]):
            # print("CASE 3")
            assert (top_left[COL] == top_right[COL]) and (bottom_left[COL] == bottom_right[COL])
            y = top_left[COL]
            for x in range(top_left[ROW], bottom_left[ROW] + 1):
                if not self.head:
                    return self.matrix
                self.matrix[x][y] = self.head.val
                self.head = self.head.next

        # Case 4: Multiple rows and multiple columns
        else:
            # print("CASE 4")
            # print(f"{top_left=}, {top_right=}, {bottom_left=}, {bottom_right=}")
            assert top_left[ROW] < bottom_left[ROW]
            assert top_left[COL] < top_right[COL]
            assert top_right[ROW] < bottom_right[ROW]
            # assert top_right[COL] > top_left[COL]
            # assert bottom_left[ROW] > top_left[ROW]
            assert bottom_left[COL] < bottom_right[COL]
            # assert bottom_right[ROW] > top_right[ROW]
            # assert bottom_right[COL] > bottom_left[COL]

            # Steps are:
            # 1) top_left -> top_right - 1
            # 2) top_right -> bottom_right - 1
            # 3) bottom_right -> bottom_left -1 
            # 4) bottom_left -> top_left -1
            

            # Step 1: top_left ---> top_right - 1
            assert top_left[ROW] == top_right[ROW]
            x = top_left[ROW]
            for y in range(top_left[COL], top_right[COL]):
                if not self.head:
                    return self.matrix
                self.matrix[x][y] = self.head.val
                self.head = self.head.next
            
            # Step 2: top_right ---> bottom_right - 1
            assert top_right[COL] == bottom_right[COL]
            y = top_right[COL]
            for x in range(top_right[ROW], bottom_right[ROW]):
                if not self.head:
                    return self.matrix
                self.matrix[x][y] = self.head.val
                self.head = self.head.next

            # Step 3: bottom_right -> bottom_left - 1
            assert bottom_right[ROW] == bottom_left[ROW]
            x = bottom_right[ROW]
            # for y in range(bottom_left[COL], bottom_right[COL] - 1):
            for y in range(bottom_right[COL], bottom_left[COL], -1):
                if not self.head:
                    return self.matrix
                self.matrix[x][y] = self.head.val
                self.head = self.head.next
            
            
            # Step 4: bottom_left -> top_left - 1
            assert top_left[COL] == bottom_left[COL]
            y = bottom_left[COL]
            for x in range(bottom_left[ROW], top_left[ROW], -1):
                if not self.head:
                    return self.matrix
                self.matrix[x][y] = self.head.val
                self.head = self.head.next
        
        # If done, return!
        if not self.head:
            return self.matrix
        
        # At this point, we just finished populating the border of the m * n matrix.
        # Since we haven't returned yet, there are still elements left to be populated
        # from the linked list. We will do this by recursively calling this function,
        # within the inner (m - 1) * (n - 1) matrix from here.
        new_top_left = (top_left[ROW] + 1, top_left[COL] + 1)
        new_top_right = (top_right[ROW] + 1, top_right[COL] - 1)
        new_bottom_left = (bottom_left[ROW] - 1, bottom_left[COL] + 1)
        new_bottom_right = (bottom_right[ROW] - 1, bottom_right[COL] - 1)
        new_corners = [new_top_left, new_top_right, new_bottom_left, new_bottom_right]
        return self.populateBorder(new_corners)
        return self.matrix
        


