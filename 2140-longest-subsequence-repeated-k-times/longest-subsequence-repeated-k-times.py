class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        res = ""
        d = defaultdict(int)
        for letter in s:
            d[letter] += 1
        # Can only use letters whose frequency is AT LEAST k
        d = {key: val for key, val in d.items() if val >= k}

        def greedy(substring: str):
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
                    continue

            # Substring only valid if found at least k occurences
            if res < k:
                return 0
            return res * len(substring)

        self.res = ""
        d = {key: freq // k for key, freq in d.items()}
        def backtrack():
            if len(d) == 0:
                return
            choices = "".join(key * d[key] for key in d)

            found_sol = False
            for perm in set(itertools.permutations(choices)):
                perm = "".join(perm)
                if greedy(perm):
                    found_sol = True
                    if len(self.res) < len(perm):
                        self.res = perm
                    elif len(self.res) == len(perm) and self.res < perm:
                        self.res = perm
            
            if found_sol:
                return
            
            for key in sorted(d.keys()):
                d[key] -= 1
                if d[key] == 0:
                    del d[key]
                
                backtrack()

                d[key] = d.get(key, 0) + 1
            

        backtrack()
        return self.res
