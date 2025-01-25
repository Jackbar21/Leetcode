class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        N = len(hand)
        if N % groupSize != 0:
            return False
        
        d = defaultdict(int) # card-to-frequency mappings
        for card in hand:
            d[card] += 1
        
        if max(d.values()) > (N // groupSize):
            return False

        # Idea: The smallest number needs to be part of a group. Call this number 'num'. Then it must
        # form a group that is num, num + 1, num + 2, ..., num + groupSize - 1. If that's not the case,
        # then we return False, otherwise we continue on over to the next group!
        # To get the smallest number each time, we will use a min_heap with the remaining numbers!
        # min_heap = [(card, freq) for card, freq in d.items()]
        min_heap = [card for card in d]
        heapq.heapify(min_heap)

        while len(min_heap) > 0:
            card = heapq.heappop(min_heap)
            freq = d[card]
            if freq == 0:
                continue

            # If have MORE than 1 of this card, will need it again later!
            if freq > 1:
                heapq.heappush(min_heap, card)

            # We must form a group of 'groupSize' consecutive cards,
            # where the starting number is 'card' as it is of SMALLEST existing value!
            for group_card in range(card, card + groupSize):
                if d[group_card] == 0:
                    return False
                d[group_card] -= 1
    
        return True
