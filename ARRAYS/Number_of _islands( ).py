# https://leetcode.com/problems/number-of-islands/submissions/1707935369/?envType=problem-list-v2&envId=array
# using breadth first search

class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        count = 0

        def bfs(r, c):
            q = deque()
            visit.add((r, c))
            q.append((r, c))
            
            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and c in range(cols)
                            and grid[r][c] == '1'
                            and (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visit:
                    bfs(r, c)
                    count += 1

        return count

----------------------------------------------------------------------------------------------------------
| Iteration | Dequeued Cell | New Neighbors Added | Queue After               | Visited Set              |
| --------- | ------------- | ------------------- | ------------------------- | ------------------------ |
| 1         | (0, 0)        | (1, 0), (0, 1)      | [(1, 0), (0, 1)]         | {(0, 0), (1, 0), (0, 1)} |
| 2         | (1, 0)        | (2, 0), (1, 1)      | [(0, 1), (2, 0), (1, 1)] | + (2, 0), (1, 1)         |
| 3         | (0, 1)        | (0, 2)              | [(2, 0), (1, 1), (0, 2)] | + (0, 2)                 |
| 4         | (2, 0)        | (2, 1)              | [(1, 1), (0, 2), (2, 1)] | + (2, 1)                 |
| 5         | (1, 1)        | —                   | [(0, 2), (2, 1)]         |                          |
| 6         | (0, 2)        | (0, 3)              | [(2, 1), (0, 3)]         | + (0, 3)                 |
| 7         | (2, 1)        | —                   | [(0, 3)]                 |                          |
| 8         | (0, 3)        | (1, 3)              | [(1, 3)]                 | + (1, 3)                 |
| 9         | (1, 3)        | —                   | []                       |                          |
----------------------------------------------------------------------------------------------------------
