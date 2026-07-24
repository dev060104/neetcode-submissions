class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        # A tree must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False

        # Build adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node):
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(0)

        # Graph is connected if every node was visited
        return len(visited) == n