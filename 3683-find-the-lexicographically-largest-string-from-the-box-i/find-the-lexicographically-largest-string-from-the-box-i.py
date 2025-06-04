class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        delete_count = numFriends - 1
        if delete_count == 0:
            return word
        
        ALPHABET = "abcdefghijklmnopqrstuvwxyz"
        freq_dict = {letter: 0 for letter in ALPHABET}
        indices_dict = {letter: [] for letter in ALPHABET}
        for index, letter in enumerate(word):
            freq_dict[letter] += 1
            indices_dict[letter].append(index)

        biggest_letter = max(letter for letter, freq in freq_dict.items() if freq > 0)
        indices = indices_dict[biggest_letter]

        res = ""
        for index in indices:
            letters_before = index
            delta = delete_count - letters_before
            case = word[index:] if delta <= 0 else word[index:-delta]
            if res < case:
                res = case
        return res
