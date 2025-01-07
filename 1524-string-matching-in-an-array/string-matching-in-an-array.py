class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        N = len(words)
        res = set()
        for i in range(N):
            for j in range(i + 1, N):
                if i == j:
                    continue
                word1, word2 = words[i], words[j]
                if word1 in word2:
                    res.add(word1)
                if word2 in word1:
                    res.add(word2)

        return list(res)