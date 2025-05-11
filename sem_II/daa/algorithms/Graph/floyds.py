class FloydWarshall:
    def __init__(self, vertices):
        self.V = vertices
        self.INF = float('inf')
        self.dist = [[self.INF for _ in range(vertices)] for _ in range(vertices)]

        for i in range(vertices):
            self.dist[i][i] = 0

    def add_edge(self, u, v, weight):
        self.dist[u][v] = weight  

    def floyd_warshall(self):
        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    if self.dist[i][j] > self.dist[i][k] + self.dist[k][j]:
                        self.dist[i][j] = self.dist[i][k] + self.dist[k][j]

    def print_solution(self):
        print("\nAll-Pairs Shortest Paths:")
        for i in range(self.V):
            for j in range(self.V):
                if self.dist[i][j] == self.INF:
                    print("INF", end="\t")
                else:
                    print(self.dist[i][j], end="\t")
            print()

def main():
    print("==== Floyd-Warshall Algorithm ====")
    V = int(input("Enter number of vertices: "))
    E = int(input("Enter number of edges: "))

    fw = FloydWarshall(V)

    print("Enter edges in format: u v weight (0-indexed):")
    for _ in range(E):
        u, v, w = map(int, input().split())
        fw.add_edge(u, v, w)

    fw.floyd_warshall()
    fw.print_solution()

if __name__ == "__main__":
    main()
