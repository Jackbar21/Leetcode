class Solution:
    def __init__(self):
        self.trie = {} # prefix_count = INT
        # self.d = {}
    def insertWord(self, word):
        trie = self.trie
        for letter in word:
            if letter not in trie:
                trie[letter] = {"pc": 0}

            trie = trie[letter]
            trie["pc"] += 1
        return
    # def isPrefix(self, word):
    def getPrefixSum(self, word):
        res = 0
        trie = self.trie
        for letter in word:
            if letter not in trie:
                break
            trie = trie[letter]
            assert "pc" in trie
            res += trie["pc"]
            
        
        return res
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        # Step 1: build a trie [O(n)]
        for word in words:
            self.insertWord(word)
        
        return map(self.getPrefixSum, words)
        # return [
        #     self.getPrefixSum(word) for word 
        # ]
        print(self.trie)
        print(self.getPrefixSum("abcd"))
        return []
        
        answer = []
        for word in words:
            res = self.getPrefixSum(word)
            answer.append(res)
        
        return answer


        # 1 .. length

        # 10^6
        # 10^3

        # for every word: # O(n)
        #         go through every prefix of that word: (1 + 2 + ... + 1000)
        #         # (1 + 2 + 3 + ... + n = n(n+1)/2 --> O(n^2))
