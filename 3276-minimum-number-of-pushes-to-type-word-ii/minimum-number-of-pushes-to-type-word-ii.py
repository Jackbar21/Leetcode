class Solution:
    def minimumPushes(self, word: str) -> int:
        letter_frequencies = [0] * 26
        for letter in word:
            letter_frequencies[ord(letter) - ord('a')] += 1
        letter_frequencies.sort(reverse=True)

        NUMBER_SLOTS = 8
        mult = NUMBER_SLOTS
        total_pushes = 0

        # O(1)
        for letter_freq in letter_frequencies:
            total_pushes += letter_freq * (mult // NUMBER_SLOTS)
            mult += 1
        
        return total_pushes

