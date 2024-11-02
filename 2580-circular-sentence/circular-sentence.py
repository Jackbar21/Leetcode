class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        arr = sentence.split(" ")
        FIRST, LAST = 0, -1

        # Handle last case first (i.e. check first and last words)
        if arr[FIRST][FIRST] != arr[LAST][LAST]:
            return False
        
        # Now check for remaining elements (except last!)
        for i in range(len(arr) - 1):
            word, next_word = arr[i], arr[i + 1]
            if word[LAST] != next_word[FIRST]:
                return False
        
        return True