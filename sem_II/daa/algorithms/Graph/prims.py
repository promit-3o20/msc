class Prims:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight  # Undirected graph

    def min_key(self, key, mst_set):
        min_val = float('inf')
        min_index = -1

        for v in range(self.V):
            if not mst_set[v] and key[v] < min_val:
                min_val = key[v]
                min_index = v
        return min_index

    def prim_mst(self):
        key = [float('inf')] * self.V
        parent = [None] * self.V
        key[0] = 0
        mst_set = [False] * self.V

        parent[0] = -1

        for _ in range(self.V):
            u = self.min_key(key, mst_set)
            mst_set[u] = True

            for v in range(self.V):
                if self.graph[u][v] != 0 and not mst_set[v] and self.graph[u][v] < key[v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.print_mst(parent)

    def print_mst(self, parent):
        print("\nMinimum Spanning Tree (MST):")
        total_weight = 0
        for i in range(1, self.V):
            print(f"{parent[i]} - {i} \tWeight: {self.graph[i][parent[i]]}")
            total_weight += self.graph[i][parent[i]]
        print(f"Total weight of MST: {total_weight}")

def main():
    print("==== Prim's Algorithm for MST ====")
    V = int(input("Enter number of vertices: "))
    E = int(input("Enter number of edges: "))
    
    g = Prims(V)
    print("Enter each edge in format: u v weight (0-indexed):")
    for _ in range(E):
        u, v, w = map(int, input().split())
        g.add_edge(u, v, w)

    g.prim_mst()

if __name__ == "__main__":
    main()
