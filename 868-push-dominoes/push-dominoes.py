class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = [char for char in dominoes]
        N = len(dominoes)
        start = 0
        last_l = None

        i = 0
        while i < N:
            dom = dominoes[i]
            if dom == ".":
                #print(f"{i=} CASE 1")
                i += 1
                continue
            
            if dom == "L":
                #print(f"{i=} CASE 2")
                last_l = i
                i += 1
                # flag = True

                for index in range(start, last_l + 1):
                    # #assert dominoes[index] != "R"
                    dominoes[index] = "L"
                start = i
                continue
            
            #assert dom == "R"
            
            # Find next left
            l = i
            # i += 1
            while i < N and dominoes[i] != "L":
                if dominoes[i] == "R":
                    for index in range(l, i):
                        dominoes[index] = "R"
                    l = i
                i += 1
            
            if i == N:
                #print(f"{i=} CASE 4")
                for index in range(l, N):
                    #assert dominoes[index] != "L"
                    dominoes[index] = "R"
                return "".join(dominoes)
            
            r = i
            #assert r < N

            #print(f"INIT: {l=}, {r=}")
            while l < r:
                #assert dominoes[l] != "L"
                #assert dominoes[r] != "R"
                dominoes[l] = "R"
                dominoes[r] = "L"
                l += 1
                r -= 1
            
            # If they met at exact point, no domino in middle fell!
            if l == r:
                dominoes[l] == "."
            # start = i + 1 - 1
            start = i + 1
            
        return "".join(dominoes)
