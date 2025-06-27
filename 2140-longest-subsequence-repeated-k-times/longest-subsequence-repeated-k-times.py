class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        res = ""
        d = defaultdict(int)
        for letter in s:
            d[letter] += 1
        # Can only use letters whose frequency is AT LEAST k
        d = {letter: freq for letter, freq in d.items() if freq >= k}

        def greedy(substring: str) -> bool:
            N = len(substring)
            res = 0
            i = 0
            substring_letter = substring[i]
            for index, letter in enumerate(s):
                if letter == substring_letter:
                    i += 1
                    if i == N:
                        i = 0
                        res += 1
                    substring_letter = substring[i]

            # Substring only valid if found at least k occurences
            return res >= k

        self.res = ""
        d = {key: freq // k for key, freq in d.items()}
        def backtrack():
            if len(d) == 0:
                return True
            choices = "".join(key * d[key] for key in d)

            for perm in sorted(map("".join, set(itertools.permutations(choices))), reverse=True):
                if greedy(perm):
                    if len(self.res) < len(perm):
                        self.res = perm
                    elif len(self.res) == len(perm) and self.res < perm:
                        self.res = perm
                    return True

            found_sol = False
            for key in sorted(d.keys()):
                d[key] -= 1
                if d[key] == 0:
                    del d[key]
                
                if backtrack():
                    found_sol = True

                d[key] = d.get(key, 0) + 1
            
            return found_sol

        backtrack()
        return self.res
