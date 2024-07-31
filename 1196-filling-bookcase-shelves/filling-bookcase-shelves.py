class Solution:
    def __init__(self):
        # HINT: Use dynamic programming: dp(i) will be the answer to the problem for books[i:].
        self.memo = {} # (i, shelf_thickness, shelf_height)
        self.books = None
        self.shelfWidth = None
    def minHeightShelvesDp(self, i):
        THICKNESS, HEIGHT = 0, 1
        if i in self.memo:
            return self.memo[i]

        if i >= len(self.books):
            return 0
        
        # book_thickness, book_height = self.books[i]

        count_books = 0
        tmp = 0
        while (
            (i + count_books) < len(self.books) and 
            tmp + self.books[i + count_books][THICKNESS] <= self.shelfWidth
        ):
            tmp += self.books[i + count_books][THICKNESS]
            count_books += 1
        
        print(f"{count_books=}, {tmp=}")
        
        # 1,2
        # 3--4
        # for j in range(1,count_books+1):

        # Case 1: only keep first book
        added_height = 0
        res = float("inf")
        for j in range(count_books): # TODO: Need the +1?
            _, book_height = self.books[i + j]
            added_height = max(added_height, book_height)
            res = min(
                res,
                added_height + self.minHeightShelvesDp(i + j + 1)
            )
        
        self.memo[i] = res
        return res

    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        # Presetup
        thickness, height = books[0]
        total_height = height
        cur_thickness = thickness
        shelf_height = height
        
        self.shelfWidth = shelfWidth
        self.books = books
        return self.minHeightShelvesDp(0)