class ProductOfNumbers:
    def __init__(self):
        self.prefix_mults = []
        self.prefix_zeroes = []
        self.N = 0

    def add(self, num: int) -> None:
        is_zero = num == 0
        mult_val = 1 if is_zero else num
        zero_val = int(is_zero)

        if self.N > 0:
            mult_val *= self.prefix_mults[-1]
            zero_val += self.prefix_zeroes[-1]
        
        self.prefix_mults.append(mult_val)
        self.prefix_zeroes.append(zero_val)
        self.N += 1

    def getProduct(self, k: int) -> int:
        index = self.N - 1 - k
        in_bounds = index >= 0

        num_zeroes = self.prefix_zeroes[-1] - (0 if not in_bounds else self.prefix_zeroes[index])
        if num_zeroes > 0:
            return 0
        
        res = self.prefix_mults[-1] // (1 if not in_bounds else self.prefix_mults[index])
        return res

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)


# nums, len(nums) == N
# prefix_sums[i] = sum(nums[0..i])

# sum(nums[i..j]) == sum(nums[0..j]) - sum(nums[0..i-1])
#                 == prefix_sums[j] - (prefix_sums[i-1] if i - 1 >= 0 else 0)

# prefix_mults[i] = product(nums[0..i])
# product(nums[i..j]) == product(nums[0..j]) / product(nums[0..i-1])