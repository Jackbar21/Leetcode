class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        d = {}
        ball_to_color = {}

        result = []
        for ball, color in queries:
            if ball in ball_to_color:
                c = ball_to_color[ball]
                assert c in d
                d[c] -= 1
                if d[c] == 0:
                    del d[c]

            ball_to_color[ball] = color
            d[color] = d.get(color, 0) + 1
            result.append(len(d))

        return result