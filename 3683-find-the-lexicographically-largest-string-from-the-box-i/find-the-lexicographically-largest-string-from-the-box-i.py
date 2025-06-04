class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        delete_count = numFriends - 1
        if delete_count == 0:
            return word
        
        ALPHABET = "abcdefghijklmnopqrstuvwxyz"
        biggest_letter = ""
        indices = []
        for index, letter in enumerate(word):
            if letter > biggest_letter:
                biggest_letter = letter
                indices = [index]
            elif letter == biggest_letter:
                indices.append(index)

        res = ""
        for index in indices:
            letters_before = index
            delta = delete_count - letters_before
            case = word[index:] if delta <= 0 else word[index:-delta]
            if res < case:
                res = case
        return res
