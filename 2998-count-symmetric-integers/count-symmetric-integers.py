class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        return sum(self.isSymmetric(num) for num in range(low, high + 1))
        
    def isSymmetric(self, num):
        str_num = str(num)
        length = len(str_num)
        if length % 2 == 1:
            return False
        
        return (
            sum(int(str_num[i]) for i in range(length // 2)) 
            == sum(int(str_num[i]) for i in range(length // 2, length))
        )