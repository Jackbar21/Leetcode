class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        res = 0
        for quantity in fruits:
            found_basket = False
            for j, capacity in enumerate(baskets):
                if quantity <= capacity:
                    baskets[j] = -1 # No longer usable
                    found_basket = True
                    break
            if not found_basket:
                res += 1
        return res
