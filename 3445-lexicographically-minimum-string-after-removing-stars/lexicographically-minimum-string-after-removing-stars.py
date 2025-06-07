class Solution:
    def clearStars(self, s: str) -> str:
        ALPHABET = "abcdefghijklmnopqrstuvwxyz"
        d = {letter: [] for letter in ALPHABET} # -1 means NO index!

        def getSmallestLetter():
            # for letter in ALPHABET:
            #     if d[letter]:
            #         return letter
            # raise Exception("No Smallest Letter")
            return next(letter for letter in d if d[letter])

        deleted_indices = set()
        for i, char in enumerate(s):
            if char == "*":
                smallest_letter = getSmallestLetter()
                deleted_indices.add(d[smallest_letter].pop())
                continue
            
            d[char].append(i)
        
        return "".join(char for i, char in enumerate(s) if char != "*" and i not in deleted_indices)