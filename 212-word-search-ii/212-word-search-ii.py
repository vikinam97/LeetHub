class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Precompute character starting positions and frequencies
        h = len(board)
        w = len(board[0])
        chars = set()
        init = DefaultDict(list)
        init_len = DefaultDict(int)
        for i in range(h):
            for j in range(w):
                chars.add(board[i][j])
                init[board[i][j]].append((i,j))
                init_len[board[i][j]] += 1
                
        # Filter out query words with characters not on board
        words = [wd for wd in words if len(set(wd) - chars) == 0]
        matched = []

        # Recursive DFS
        def search(word, i, visited):
            if i == len(word):
                return True
            y, x = visited[-1]
            fwd = []
            if y - 1 >= 0 and word[i] == board[y-1][x]:
                fwd.append((y - 1, x))
            if y + 1 < h and word[i] == board[y+1][x]:
                fwd.append((y + 1, x))
            if x - 1 >= 0 and word[i] == board[y][x-1]:
                fwd.append((y, x - 1))
            if x + 1 < w and word[i] == board[y][x+1]:
                fwd.append((y, x + 1))
            for v in fwd:
                if v in visited:
                    continue
                if search(word, i+1, visited[:] + [v]):
                    return True
        
        # Search wrapper per word
        def exist(word: str) -> bool:
            # Edge case
            if len(chars) == 1:
                if len(word) <= w*h:
                    return True
            
			# MAIN OPTIMIZATION:
            # If second half of word has rarer characters than first,
            # search for reverse string
            tword = word
            mid = len(word) // 2
            if sum([init_len[c] for c in word[mid:]]) < sum([init_len[c] for c in word[:mid]]): 
                tword = word[::-1]
            for l in init[tword[0]]:
                if search(tword, 1, [l]):
                    return True
                
        # Process filtered list
        for wd in words:
            if exist(wd):
                matched.append(wd)
                    
        return matched