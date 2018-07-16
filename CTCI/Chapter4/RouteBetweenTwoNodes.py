def bfs_shortest_path(graph, start,end):
    visited = []
    queue = [start]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in visited:
        	neighbours = graph [node]
        	visited.append(node)
        	for x in neighbours:
        		new_path = list(path)
        		new_path.append(x)
        		queue.append(new_path)
        		if x==end:
        			return new_path


    return 'No path exists'

if __name__ == "__main__":
	graph = {'A': ['B', 'C', 'E'],
	         'B': ['A','D', 'E'],
	         'C': ['A', 'F', 'G'],
	         'D': ['B'],
	         'E': ['A', 'B','D'],
	         'F': ['C'],
	         'G': ['C','E']}
	print bfs_shortest_path(graph,'G','E')