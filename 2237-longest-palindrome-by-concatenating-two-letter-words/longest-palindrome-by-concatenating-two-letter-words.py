class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        d = {}
        for word in words:
            d[word] = d.get(word, 0) + 1
        res = 0
        equal_letters = defaultdict(int)
        # while len(words) > 0:
        for word in words:
            if d.get(word, 0) <= 0:
                assert d.get(word, 0) == 0
                continue

            assert d[word] >= 1
            d[word] -= 1
            if d[word] == 0:
                del d[word]

            assert len(word) == 2
            letter_a, letter_b = word
            # print(f"{letter_a=}, {letter_b=}, {letter_b + letter_a=}, {(letter_b + letter_a) in words=}")
            if letter_a == letter_b:
                # res += 2
                equal_letters[word] += 1
                continue
            elif (other_word := letter_b + letter_a) in d:
                # words.remove(letter_b + letter_a)
                d[other_word] -= 1
                if d[other_word] == 0:
                    del d[other_word]
                res += 4
        
        # print(f"{res=}, {equal_letters=}")
        res += 4 * sum(freq // 2 for freq in equal_letters.values())
        res += 2 * any(freq % 2 == 1 for freq in equal_letters.values())

        return res
        
