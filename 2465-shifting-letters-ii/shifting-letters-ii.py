class Solution:
    def mutateLetter(self, letter, delta):
        if delta == 0:
            return letter
        
        val = ord(letter) - self.ORD_A
        val += delta
        val %= 26
        return self.alphabet[val]

    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.ORD_A = ord("a")
        # val = self.mutateLetter("a", 0)
        # print(f"{val=}")
        # return ""
        line_sweep = [0] * (len(s) + 1)
        for start, end, direction in shifts:
            l, r = (-1, 1) if direction == 0 else (1, -1)
            line_sweep[start] += l
            line_sweep[end + 1] += r
        
        # print(f"{line_sweep=}")
        mutate = 0
        new_s = []
        for i in range(len(s)):
            mutate += line_sweep[i]
            mutated_letter = self.mutateLetter(s[i], mutate)
            new_s.append(mutated_letter)



        # TODO: Modify new_s based on line_sweep
        return "".join(new_s)