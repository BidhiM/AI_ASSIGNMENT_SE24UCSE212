from collections import deque

class RiverProblem:
    def __init__(self):
        self.start = (3, 3, 1) #missionary,cannibal and boat all on the left
        self.goal = (0, 0, 0)

    def is_valid(self, m, c):
        if m < 0 or c < 0 or m > 3 or c > 3: return False
        if m > 0 and m < c: return False 
        if 3 - m > 0 and (3 - m) < (3 - c): return False 
        return True

    def get_successors(self, state):
        m, c, boat = state
        moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]
        next_states = []
        for dm, dc in moves:
            if boat == 1: 
                new_s = (m - dm, c - dc, 0)
            else: 
                new_s = (m + dm, c + dc, 1)
            if self.is_valid(new_s[0], new_s[1]):
                next_states.append(new_s)
        return next_states

    def search(self, strategy="BFS", limit=None):
        frontier = deque([(self.start, [self.start])])
        visited = {} 

        while frontier:
            state, path = frontier.popleft() if strategy == "BFS" else frontier.pop()
            
            if state == self.goal: return path
     
            if limit is not None and len(path) > limit: continue
            
            if state in visited and visited[state] <= len(path): continue
            visited[state] = len(path)

            for next_s in self.get_successors(state):
                frontier.append((next_s, path + [next_s]))
        return None

    def iddfs(self, max_depth=20):
        for depth in range(max_depth):
            result = self.search(strategy="DFS", limit=depth)
            if result: return result, depth
        return None, max_depth

problem = RiverProblem()
print(f"BFS Solution: {problem.search('BFS')}")
print(f"DLS (limit 12) Solution: {problem.search('DFS', limit=12)}")
iddfs_sol, d = problem.iddfs()
print(f"IDDFS Solution (found at depth {d}): {iddfs_sol}")
