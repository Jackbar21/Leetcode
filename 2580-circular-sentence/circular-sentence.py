class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        # print(f"{sentence=}")
        words = sentence.split(" ")
        # print(f"{words=}")
        FIRST, LAST = 0, -1

        # Handle last case first (i.e. check first and last words)
        # if words[FIRST][FIRST] != words[LAST][LAST]:
        #     return False
        words.append(words[FIRST])
        
        # Now check for remaining elements (except last!)
        for i in range(len(words) - 1):
            word, next_word = words[i], words[i + 1]
            if word[LAST] != next_word[FIRST]:
                return False
        
        return True