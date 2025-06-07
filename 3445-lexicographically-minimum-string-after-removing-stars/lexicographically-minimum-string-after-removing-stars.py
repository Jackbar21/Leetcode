class Solution:
    def clearStars(self, s: str) -> str:
        ALPHABET = "abcdefghijklmnopqrstuvwxyz"
        ORD_A = ord("a")
        # d = {letter: [] for letter in ALPHABET} # -1 means NO index!
        d = [[] for _ in range(len(ALPHABET))]
        letter_to_index = lambda letter: ord(letter) - ORD_A

        def getSmallestLetter():
            for i, arr in enumerate(d):
                if arr:
                    return ALPHABET[i]
            # Should always exist a solution!
            assert False

        deleted_indices = set()
        for i, char in enumerate(s):
            if char == "*":
                smallest_letter = getSmallestLetter()
                deleted_indices.add(d[letter_to_index(smallest_letter)].pop())
                continue
            
            d[letter_to_index(char)].append(i)
        
        return "".join(char for i, char in enumerate(s) if char != "*" and i not in deleted_indices)