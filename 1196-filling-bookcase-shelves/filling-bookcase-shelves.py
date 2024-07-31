class Solution:
    def __init__(self):
        self.memo = {}
        self.books = None
        self.shelfWidth = None
    def minHeightShelvesDp(self, i):
        if i in self.memo:
            return self.memo[i]

        if i >= len(self.books):
            return 0

        count_books = 0
        tmp = 0
        while (
            (i + count_books) < len(self.books) and 
            tmp + self.books[i + count_books][0] <= self.shelfWidth
        ):
            tmp += self.books[i + count_books][0]
            count_books += 1
        
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
        self.shelfWidth = shelfWidth
        self.books = books
        return self.minHeightShelvesDp(0)