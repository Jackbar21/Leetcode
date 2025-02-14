class ProductOfNumbers:

    def __init__(self):
        self.prefix_mults = []
        self.num_zeroes = []

    def add(self, num: int) -> None:
        self.prefix_mults.append((1 if num == 0 else num) * (1 if len(self.prefix_mults) == 0 else self.prefix_mults[-1]))
        self.num_zeroes.append((num == 0) + (0 if len(self.num_zeroes) == 0 else self.num_zeroes[-1]))

    def getProduct(self, k: int) -> int:
        # return functools.reduce(lambda acc, x: acc * x, self.queue[-k:], 1)
        # print(f"{self.prefix_mults=}")
        numerator = self.prefix_mults[-1]
        denominator = (self.prefix_mults[len(self.prefix_mults) - 1 - k] if len(self.prefix_mults) - 1 - k >= 0 else 1)

        num_zeroes = self.num_zeroes[-1] - (self.num_zeroes[len(self.num_zeroes) - 1 - k] if len(self.prefix_mults) - 1 - k >= 0 else 0)
        assert num_zeroes >= 0
        if num_zeroes > 0:
            return 0
        # if denominator == 0:
        #     return 0
        return numerator // denominator


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)