class Solution:
    def clearStars(self, s: str) -> str:
        ALPHABET = "abcdefghijklmnopqrstuvwxyz"
        d = {letter: [] for letter in ALPHABET} # -1 means NO index!

        def getSmallestLetter():
            for letter in ALPHABET:
                if d[letter]:
                    return letter
            raise Exception("No Smallest Letter")

        deleted_indices = []
        for i, char in enumerate(s):
            if char == "*":
                smallest_letter = getSmallestLetter()
                deleted_indices.append(d[smallest_letter].pop())
                deleted_indices.append(i) # Don't include stars in solution!
                continue
            
            d[char].append(i)
        
        deleted_indices.sort()
        # print(f"{deleted_indices=}")
        N = len(deleted_indices)
        if N == 0:
            return s
        arr_index = 0
        arr_val = deleted_indices[arr_index]
        res = []
        for i, char in enumerate(s):
            if i == arr_val:
                arr_index += 1
                if arr_index < N:
                    arr_val = deleted_indices[arr_index]
                continue
            
            res.append(char)
        
        return "".join(res)


