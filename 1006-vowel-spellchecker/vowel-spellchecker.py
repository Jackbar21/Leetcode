class Solution(object):
    def spellchecker(self, wordlist, queries):
        def devowel(word):
            return "".join('*' if c in 'aeiou' else c
                           for c in word)

        words_perfect = set(wordlist)
        words_cap = {}
        words_vow = {}

        for word in wordlist:
            wordlow = word.lower()
            words_cap.setdefault(wordlow, word)
            words_vow.setdefault(devowel(wordlow), word)

        def solve(query):
            if query in words_perfect:
                return query

            queryL = query.lower()
            if queryL in words_cap:
                return words_cap[queryL]

            queryLV = devowel(queryL)
            if queryLV in words_vow:
                return words_vow[queryLV]
            return ""

        return list(map(solve, queries))

# ATTEMPT
# class Trie:
#     def __init__(self):
#         self.trie = {}
#         self.vowels = list("aeiou")

#     def insert(self, word: str) -> None:
#         trie = self.trie
#         for letter in word:
#             if letter not in trie:
#                 trie[letter] = {}
#             trie = trie[letter]
#         trie["."] = word

# class Solution:
#     def search(self, trie: dict, word: str, index: int) -> bool:
#         assert 0 <= index <= len(word)
#         if index == len(word):
#             return trie["."]

#         letter = word[index]

#         valid_letters = [letter, letter.lower() if letter != letter.lower() else letter.upper()]
#         if letter in "aeiouAEIOU":
#             valid_letters.extend(list("aeiouAEIOU"))
        
#         for valid_letter in valid_letters:
#             if valid_letter in trie:
#                 res = self.search(trie[valid_letter], word, index + 1)
#                 if res != "":
#                     return res
#         return ""
#     def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
#         trie = Trie()
#         for word in wordlist:
#             trie.insert(word)
#         trie_dict = trie.trie

#         res = []
#         for query in queries:
#             res.append(self.search(trie_dict, query, 0))
#         return res
