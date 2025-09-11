class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = sorted("aeiouAEIOU", key = lambda letter: ord(letter), reverse = False)
        arr = []
        vowel_counts = {vowel: 0 for vowel in vowels}
        vowel_indices = []
        for i, char in enumerate(s):
            if char in vowels:
                vowel_counts[char] += 1
                vowel_indices.append(i)
            arr.append(char)
        
        index = 0
        for vowel in vowels:
            for _ in range(vowel_counts[vowel]):
                arr[vowel_indices[index]] = vowel
                index += 1
        
        return "".join(arr)