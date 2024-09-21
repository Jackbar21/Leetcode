class Solution:
    def __init__(self):
        self.n = None
        self.res = []
    def explore(self, starting_digit):
        root = TreeNode(starting_digit)
        num = starting_digit * 10
        while num <= self.n:
            return

    def dfs(self, i):
        if i > self.n:
            return

        # print(f"{i=}")
        self.res.append(i)
        # self.dfs(i * 10)
        for j in range(10):
            self.dfs(i * 10 + j)


    def lexicalOrder(self, n: int) -> List[int]:
        # return sorted(range(1, n + 1), key=lambda num: str(num))
        self.n = n
        # self.dfs(1)
        # return []
        for starting_digit in range(1, 9 + 1):
            self.dfs(starting_digit)
        return self.res
        
        # res = []
        for starting_digit in range(1, 9 + 1):
            stack = [starting_digit]
            base = 1
            # num = starting_digit * 10
            while num <= n:
                num = stack[-1] * 10
                for i in range(10):
                    if num > n:
                        break
                    stack.append(num + i)
            
                


        # starting_digits = [str(digit) for digit in range(1, 9 + 1)]
        # for starting_digit in starting_digits:
        for starting_digit in range(1, 9 + 1):
            # print(starting_digit)
            # e.g. starting_digit == 1
            base = 1 # keep multiplying by 10
            num = starting_digit * base
            while num <= n:
                # res.append(num)
                for _ in range(base):
                # for _ in range(min(base, n - num + 1)):
                    if num <= n:
                        res.append(num)
                        num += 1
                    # if num > n:
                    #     break
                base *= 10
                num = starting_digit * base
            
        return res
            
