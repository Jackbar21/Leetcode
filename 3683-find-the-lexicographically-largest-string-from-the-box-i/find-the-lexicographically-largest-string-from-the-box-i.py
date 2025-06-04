class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        delete_count = numFriends - 1
        # if numFriends == 1:
        #     return word
        if delete_count == 0:
            return word
        
        ALPHABET = "abcdefghijklmnopqrstuvwxyz"
        # ORD_A = ord("a")
        # getLetterIndex = lambda letter: ord(letter) - ORD_A
        # freq = [0] * len(ALPHABET)
        # for letter in word:
        #     freq[getLetterIndex(letter)] += 1
        # getLetterFreq = lambda letter: freq[getLetterIndex(letter)]
        freq_dict = {letter: 0 for letter in ALPHABET}
        indices_dict = {letter: [] for letter in ALPHABET}
        for index, letter in enumerate(word):
            freq_dict[letter] += 1
            indices_dict[letter].append(index)

        biggest_letter = max(word)
        indices = indices_dict[biggest_letter]

        res = ""
        for index in indices:
            letters_before = index
            delta = delete_count - letters_before
            case = word[index:] if delta <= 0 else word[index:-delta]
            res = max(res, case)
        return res
