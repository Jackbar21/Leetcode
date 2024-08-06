class Solution:
    def minimumPushes(self, word: str) -> int:
        d = {}
        for letter in word:
            d[letter] = d.get(letter, 0) + 1

        number_slots = 8 # Constant
        multiplier = number_slots
        total_pushes = 0

        # O(1)
        for letter in sorted(d.keys(), key=lambda key: d[key], reverse=True):
            letter_freq = d[letter]
            total_pushes += letter_freq * (multiplier // number_slots)
            multiplier += 1
        
        return total_pushes

