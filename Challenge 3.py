import time

start_time= time.time()


# Representasi graf sebagai adjacency list
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E', 'G'],
    'C': ['A', 'E', 'F'],
    'D': ['A', 'F', 'J'],
    'E': ['B', 'C', 'H', 'K'],
    'F': ['C', 'D', 'I', 'K'],
    'G': ['B', 'H', 'K'],
    'H': ['E', 'G', 'K'],
    'I': ['F', 'J', 'K'],
    'J': ['D', 'I', 'K'],
    'K': ['E', 'F', 'G', 'H', 'I', 'J']
}

# Fungsi mencari semua path dari start ke end
def find_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]

    paths = []
    for node in graph[start]:
        if node not in path:  # Menghindari loop
            new_paths = find_paths(graph, node, end, path)
            paths.extend(new_paths)
    
    return paths

# Fungsi mencari semua cycle dari titik tertentu
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

# Fungsi mencari circuit terpendek dan terpanjang dari start ke end
def find_circuits(graph, start, end, path=[]):
    path = path + [start]
    if start == end and len(path) > 1:
        return [path]

    circuits = []
    for node in graph[start]:
        if node not in path or node == end:  # Mengizinkan mengulang tujuan
            new_circuits = find_circuits(graph, node, end, path)
            circuits.extend(new_circuits)

    return circuits

# Mencari path sesuai challenge
paths_A_K = find_paths(graph, 'A', 'K')
paths_G_J = find_paths(graph, 'G', 'J')
paths_G_E = find_paths(graph, 'G', 'E')

# Mencari cycle sesuai challenge
cycles_A = find_cycles(graph, 'A')
cycles_K = find_cycles(graph, 'K')

# Mencari circuit terpendek dan terpanjang
circuits_A_K = find_circuits(graph, 'A', 'K')
circuits_G_J = find_circuits(graph, 'G', 'J')
circuits_E_F = find_circuits(graph, 'E', 'F')

# Menampilkan hasil
print("Paths dari A ke K:")
for path in paths_A_K:
    print(path)

print("\nPaths dari G ke J:")
for path in paths_G_J:
    print(path)

print("\nPaths dari G ke E:")
for path in paths_G_E:
    print(path)

print("\nCycles yang dimulai dari A:")
for cycle in cycles_A:
    print(cycle)

print("\nCycles yang dimulai dari K:")
for cycle in cycles_K:
    print(cycle)

if circuits_A_K:
    print("\nCircuit Terpendek dari A ke K:", min(circuits_A_K, key=len))
    print("Circuit Terpanjang dari A ke K:", max(circuits_A_K, key=len))

if circuits_G_J:
    print("\nCircuit Terpendek dari G ke J:", min(circuits_G_J, key=len))
    print("Circuit Terpanjang dari G ke J:", max(circuits_G_J, key=len))

if circuits_E_F:
    print("\nCircuit Terpendek dari E ke F:", min(circuits_E_F, key=len))
    print("Circuit Terpanjang dari E ke F:", max(circuits_E_F, key=len))



end_time= time.time()
execution_time = end_time - start_time
print(f"Waktu eksekusi: {execution_time:.6f} detik")