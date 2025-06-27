class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        res = ""
        d = defaultdict(int)
        for letter in s:
            d[letter] += 1
        # Can only use letters whose frequency is AT LEAST k
        d = {key: val for key, val in d.items() if val >= k}
        # print(f"{d=}")

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
                
                # remaining_letter_count = len(s) - index
                # needed_letter_count = (N - i) + len(substring) * res
                # if remaining_letter_count < needed_letter_count:
                #     return 0
            
            # Substring only valid if found at least k occurences
            if res < k:
                return 0
            return res * len(substring)


        self.res = ""
        # mergeLists = lambda arr: functools.reduce(lambda arr1, arr2: arr1 + arr2, arr, [])
        # d = [(key, freq // k) for key, freq in d.items()]
        d = {key: freq // k for key, freq in d.items()}
        print(f"TRUTH: {d=}")
        def backtrack():
            if len(d) == 0:
                return True

            # choices = "".join(mergeLists([key] * (freq // k) for key, freq in d.items()))
            choices = "".join(key * d[key] for key in d)
            # if len(choices) < len(self.res):
            #     return
            # print
            for perm in sorted(set(itertools.permutations(choices)), reverse = True):
                perm = "".join(perm)
                # if perm in ["babab", "bbbb"]:
                print(f"{perm=}")
                if greedy(perm):
                    # print(f"NEW SOL: {perm}")
                    # self.res = max(self.res, perm)
                    if len(self.res) < len(perm):
                        self.res = perm
                    elif len(self.res) == len(perm) and self.res < perm:
                        self.res = perm
                    return True
            
            for key in sorted(d.keys()):
                d[key] -= 1
                if d[key] == 0:
                    del d[key]
                
                # if backtrack():
                    # return True
                backtrack()

                if key not in d:
                    d[key] = 1
                else:
                    d[key] += 1
            
            return False


        # while len(d) > 0:
        #     choices = mergeLists([key] * (freq // k) for key, freq in d.items())
        #     for perm in itertools.permutations(choices):
        #         print(f"{perm=}")
        #     print()


        # print(f"{choices=}")
        backtrack()
        return self.res
