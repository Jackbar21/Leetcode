class Solution:
    def isHappy(self, n: int) -> bool:
        str_n = str(n)
        visited = set()
        while str_n != "1":
            if str_n in visited:
                return False

            visited.add(str_n)
            str_n = str(sum(pow(int(digit), 2) for digit in str_n))
        
        return True