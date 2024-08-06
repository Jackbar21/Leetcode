class Solution:
    def minimumPushes(self, word: str) -> int:
        d = {}
        for letter in word:
            d[letter] = d.get(letter, 0) + 1

        arr = sorted(d.keys(), key=lambda key: d[key], reverse=True)

        number_slots = 8 # Constant
        multiplier = number_slots
        total_pushes = 0

        for letter in arr:
            letter_freq = d[letter]
            total_pushes += letter_freq * (multiplier // number_slots)
            multiplier += 1
        
        return total_pushes

