class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = [-1] * len(prices)

        stack = [(-1, float("-inf"))] # dummy value
        for j, price_j in enumerate(prices):
            while True:
                i, price_i = stack[-1]
                if price_j <= price_i:
                    stack.pop()
                    answer[i] = price_i - price_j
                    continue
                else:
                    stack.append((j, price_j))
                    break
        
        while len(stack) > 1: # since first value is dummy value!
            index, full_price = stack.pop()
            answer[index] = full_price # No discount!
        
        return answer