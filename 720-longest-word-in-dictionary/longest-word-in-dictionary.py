class Solution:
    def longestWord(self, words: List[str]) -> str:
        # Assumption: must start at one letter
        # I will build a dependency graph, where nodes are the words in 'words',
        # and an edge exists from node u to node v if and only if node u is a 
        # prefix of word v except for the last character exactly.
        nodes = set(words)
        adj_list = defaultdict(list)
        for word in words:
            prefix = word[:len(word) - 1] # Constraints make max word length 30, so this is okay!
            if prefix in nodes:
                adj_list[prefix].append(word)
        
        queue = collections.deque([word for word in words if len(word) == 1])
        res = ""

        # Visited set is not needed, since this graph is a DAG
        while queue:
            word = queue.popleft()
            if len(word) > len(res):
                res = word
            elif len(word) == len(res) and res > word:
                res = word
            
            for neigh in adj_list[word]:
                queue.append(neigh)
        
        return res