class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        assert len(names) == len(heights)
        pairs = [(names[i], heights[i]) for i in range(len(names))]
        pairs.sort(key = lambda pair: pair[1], reverse=True)
        return [pair[0] for pair in pairs]
