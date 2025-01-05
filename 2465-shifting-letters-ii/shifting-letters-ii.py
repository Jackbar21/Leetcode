class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        ALPHABET, ORD_A = "abcdefghijklmnopqrstuvwxyz", ord("a")
        mutateLetter = lambda letter, delta: ALPHABET[(ord(letter) - ORD_A + delta) % 26]
        line_sweep = [0] * (len(s) + 1)
        for start, end, direction in shifts:
            l, r = (-1, 1) if direction == 0 else (1, -1)
            line_sweep[start] += l
            line_sweep[end + 1] += r
        
        mutate = 0
        new_s = [letter for letter in s]
        for i in range(len(s)):
            mutate += line_sweep[i]
            if mutate != 0:
                mutated_letter = mutateLetter(s[i], mutate)
                new_s[i] = mutated_letter

        return "".join(new_s)

# interval = [i, j]

# mutate = 0
# line_sweep = [0,0,0,0,0,0,-1,0,0,-1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0]
#                           i                 j+1