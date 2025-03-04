from itertools import permutations
import time

start_time= time.time()

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = find_all_paths(graph, node, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths

def find_cycles(graph, start, path=[]):
    path = path + [start]
    cycles = []
    for node in graph[start]:
        if node in path:
            cycle_index = path.index(node)
            cycles.append(path[cycle_index:] + [node])
        else:
            new_cycles = find_cycles(graph, node, path)
            for cycle in new_cycles:
                cycles.append(cycle)
    return cycles

# Definisi graf berdasarkan gambar
graph = {
    'A': ['D', 'E'],
    'B': ['C', 'E', 'D'],
    'C': ['F'],
    'D': ['A', 'B', 'E', 'F'],
    'E': ['A', 'B', 'D', 'F'],
    'F': ['C', 'D', 'E']
}

# Menemukan semua path dari A ke C
all_paths = find_all_paths(graph, 'A', 'C')
print("Semua path dari A ke C:")
for path in all_paths:
    print(path)

# Menemukan semua cycle jika C adalah titik awal
print("\nSemua cycle jika C adalah titik awal:")
cycles_from_C = find_cycles(graph, 'C')
for cycle in cycles_from_C:
    print(cycle)

# Menemukan semua cycle jika B adalah titik awal
print("\nSemua cycle jika B adalah titik awal:")
cycles_from_B = find_cycles(graph, 'B')
for cycle in cycles_from_B:
    print(cycle)

# Menentukan circuit terpendek dan terpanjang dari A ke C
shortest_path = min(all_paths, key=len)
longest_path = max(all_paths, key=len)
print("\nCircuit terpendek dari A ke C:", shortest_path)
print("Circuit terpanjang dari A ke C:", longest_path)

end_time= time.time()
execution_time = end_time - start_time
print(f"Waktu eksekusi: {execution_time:.6f} detik")