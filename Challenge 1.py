from itertools import permutations
import time

start_time=time.time()
# Definisikan graf sebagai dictionary adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

# 1. Mencari semua trail dari A ke D
def find_trails(graph, start, end, path=[], visited_edges=set()):
    path = path + [start]
    if start == end:
        return [path]
    
    trails = []
    for node in graph[start]:
        edge = frozenset([start, node])
        if edge not in visited_edges:
            new_visited_edges = visited_edges | {edge}
            new_trails = find_trails(graph, node, end, path, new_visited_edges)
            trails.extend(new_trails)
    
    return trails

trails = find_trails(graph, 'A', 'D')
print("Trails dari A ke D:")
for trail in trails:
    print(trail)

# 2. Mencari semua path dari A ke D
def find_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    
    paths = []
    for node in graph[start]:
        if node not in path:  # Path tidak boleh mengulang simpul
            new_paths = find_paths(graph, node, end, path)
            paths.extend(new_paths)
    
    return paths

paths = find_paths(graph, 'A', 'D')
print("\nPaths dari A ke D:")
for path in paths:
    print(path)

# 3. Mencari semua cycle yang dimulai dari A
def find_cycles(graph, start, path=[], visited_edges=set()):
    path = path + [start]
    cycles = []
    for node in graph[start]:
        if node == path[0] and len(path) > 2:
            cycles.append(path + [node])
        elif node not in path:
            edge = frozenset([start, node])
            if edge not in visited_edges:
                new_visited_edges = visited_edges | {edge}
                new_cycles = find_cycles(graph, node, path, new_visited_edges)
                cycles.extend(new_cycles)
    return cycles

cycles = find_cycles(graph, 'A')
print("\nCycles yang dimulai dari A:")
for cycle in cycles:
    print(cycle)

end_time= time.time()
execution_time = end_time - start_time
print(f"Waktu eksekusi: {execution_time:.6f} detik")