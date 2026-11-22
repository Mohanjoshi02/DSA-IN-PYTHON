"""Practical 9A: Minimum spanning tree using Kruskal's and Prim's algorithms."""

import heapq


class DisjointSet:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, first, second):
        first_root, second_root = self.find(first), self.find(second)
        if first_root == second_root:
            return False
        if self.rank[first_root] < self.rank[second_root]:
            first_root, second_root = second_root, first_root
        self.parent[second_root] = first_root
        if self.rank[first_root] == self.rank[second_root]:
            self.rank[first_root] += 1
        return True


def kruskal(vertex_count, edges):
    forest = DisjointSet(vertex_count)
    tree = []
    for first, second, weight in sorted(edges, key=lambda edge: edge[2]):
        if forest.union(first, second):
            tree.append((first, second, weight))
    if len(tree) != max(0, vertex_count - 1):
        raise ValueError("The graph must be connected.")
    return tree


def prim(vertex_count, edges, start=0):
    graph = [[] for _ in range(vertex_count)]
    for first, second, weight in edges:
        graph[first].append((weight, second))
        graph[second].append((weight, first))
    visited = {start}
    pending = [(weight, start, neighbour) for weight, neighbour in graph[start]]
    heapq.heapify(pending)
    tree = []
    while pending and len(tree) < vertex_count - 1:
        weight, first, second = heapq.heappop(pending)
        if second in visited:
            continue
        visited.add(second)
        tree.append((first, second, weight))
        for next_weight, neighbour in graph[second]:
            if neighbour not in visited:
                heapq.heappush(pending, (next_weight, second, neighbour))
    if len(tree) != max(0, vertex_count - 1):
        raise ValueError("The graph must be connected.")
    return tree


def main():
    vertex_count = int(input("Number of vertices: "))
    edge_count = int(input("Number of edges: "))
    edges = []
    for _ in range(edge_count):
        first, second, weight = map(
            int, input("Enter an edge (u v weight): ").split()
        )
        edges.append((first, second, weight))
    algorithm = input("Choose algorithm (Kruskal/Prim): ").strip().lower()
    tree = kruskal(vertex_count, edges) if algorithm == "kruskal" else prim(vertex_count, edges)
    print("Minimum spanning tree:")
    print("Edge\tWeight")
    for first, second, weight in tree:
        print(f"{first} - {second}\t{weight}")
    print("Total cost:", sum(weight for _, _, weight in tree))


if __name__ == "__main__":
    main()
