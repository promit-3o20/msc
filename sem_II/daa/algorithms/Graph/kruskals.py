class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight

class Kruskal:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append(Edge(u, v, weight))

    def find_parent(self, parent, i):
        if parent[i] == i:
            return i
        return self.find_parent(parent, parent[i]) 

    def union(self, parent, rank, x, y):
        xroot = self.find_parent(parent, x)
        yroot = self.find_parent(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_mst(self):
        result = []
        self.edges.sort(key=lambda e: e.weight)

        parent = [i for i in range(self.V)]
        rank = [0] * self.V

        for edge in self.edges:
            x = self.find_parent(parent, edge.u)
            y = self.find_parent(parent, edge.v)

            if x != y:
                result.append(edge)
                self.union(parent, rank, x, y)

        print("\nMinimum Spanning Tree (MST) by Kruskal's Algorithm:")
        total_weight = 0
        for edge in result:
            print(f"{edge.u} - {edge.v} \tWeight: {edge.weight}")
            total_weight += edge.weight
        print(f"Total weight of MST: {total_weight}")

def main():
    print("==== Kruskal's Algorithm for MST ====")
    V = int(input("Enter number of vertices: "))
    E = int(input("Enter number of edges: "))

    k = Kruskal(V)
    print("Enter edges in format: u v weight (0-indexed):")
    for _ in range(E):
        u, v, w = map(int, input().split())
        k.add_edge(u, v, w)

    k.kruskal_mst()

if __name__ == "__main__":
    main()
