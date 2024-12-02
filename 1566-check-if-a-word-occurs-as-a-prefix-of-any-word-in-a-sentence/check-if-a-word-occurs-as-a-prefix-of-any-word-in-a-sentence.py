class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i, word in enumerate(sentence.split(" ")):
            # if word.startswith(searchWord):
            #     return i
            if len(word) < len(searchWord):
                continue

            is_prefix = True
            for index in range(len(searchWord)):
                if word[index] != searchWord[index]:
                    is_prefix = False
                    break

            if is_prefix:
                return i + 1

        return -1