class Solution:
    def isHappy(self, n: int) -> bool:
        str_n = str(n)
        visited = set()
        while str_n not in visited:
            visited.add(str_n)
            str_n = str(sum(pow(int(digit), 2) for digit in str_n))
            if str_n == "1":
                return True
        
        return False