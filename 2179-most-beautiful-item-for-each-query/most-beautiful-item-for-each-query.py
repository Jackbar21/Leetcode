class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        PRICE, BEAUTY = 0, 1
        items.sort(key = lambda item: item[PRICE])

        prefix_beauties = []
        max_beauty = float("-inf")

        for (_, beauty) in items:
            max_beauty = max(max_beauty, beauty)
            prefix_beauties.append(max_beauty)
        
        answer = []
        for price in queries:
            # Rightmost binary search on prices
            l, r = 0, len(items) - 1
            ans = 0
            while l <= r:
                mid = (l + r) // 2
                if items[mid][PRICE] <= price:
                    # Valid price, update ans, and search for even better ones!
                    ans = max(ans, prefix_beauties[mid])
                    l = mid + 1
                else:
                    r = mid - 1
            answer.append(ans)

        return answer
