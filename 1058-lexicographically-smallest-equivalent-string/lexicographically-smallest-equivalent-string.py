class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        assert len(s1) == len(s2)
        N = len(s1)
        ALPHABET = "abcdefghijklmnopqrstuvwxyz"

        # Step 1: Create graph out of letter equality relationship
        # (e.g. edge from letter X to letter Y means X == Y)
        adj_list = {letter: [] for letter in ALPHABET}
        for i in range(N):
            letter1, letter2 = s1[i], s2[i]
            adj_list[letter1].append(letter2)
            adj_list[letter2].append(letter1)
        
        # Step 2: There are a constant amount of English lowercase letters, namely 26.
        # For each such letter, run a bfs traversal to find the lexicographically SMALLEST
        # letter it can map to.
        # NOTE: We run a BFS from each letter and not leverage DP amongst one another, 
        # since this graph contains CYCLES. But since only O(1) unique letters, this is okay!
        best_letter = {letter: letter for letter in ALPHABET}
        for source_letter in ALPHABET:
            # Run BFS
            queue = collections.deque([source_letter])
            visited = set([source_letter])
            smallest_letter = source_letter
            while queue:
                letter = queue.pop()
                if letter < smallest_letter:
                    smallest_letter = letter
                if smallest_letter == "a":
                    break
                
                for neigh in adj_list[letter]:
                    if neigh not in visited:
                        visited.add(neigh)
                        queue.append(neigh)
            
            # Update res once BFS is finished!
            best_letter[source_letter] = smallest_letter
        
        return "".join(best_letter[letter] for letter in baseStr)
