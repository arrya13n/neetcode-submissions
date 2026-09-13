class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        component_count = 0

        graph_dict = {i: [] for i in range(n)}

        for n1,n2 in edges:
            graph_dict[n1].append(n2)
            graph_dict[n2].append(n1)
        
        visited_node = set()

        def dfs(i):
            for neighbor in graph_dict[i]:
                if neighbor not in visited_node:
                    visited_node.add(neighbor)
                    dfs(neighbor)
        
        for i in graph_dict:
            if i in visited_node:
                continue
            else:
                visited_node.add(i)
                component_count += 1
                dfs(i)
        return component_count
