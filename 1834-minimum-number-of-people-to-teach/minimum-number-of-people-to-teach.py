class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        # Convert each user's languages into a set for quick lookup
        languages = list(map(lambda language_list: set(language_list), languages))

        # Step 1: Find all friendships where users cannot talk
        cannot_talk = set()
        for u, v in friendships:
            if languages[u - 1].isdisjoint(languages[v - 1]):  # No common language
                cannot_talk.add(u - 1)
                cannot_talk.add(v - 1)

        # If everyone can already communicate, no teaching needed
        if not cannot_talk:
            return 0

        # Step 2: Try teaching each language to the "cannot_talk" users
        res = float("inf")
        for lang in range(1, n + 1):
            # Count how many in cannot_talk don’t know this language
            need_teach = sum(1 for user in cannot_talk if lang not in languages[user])
            if need_teach < res:
                res = need_teach

        return res
