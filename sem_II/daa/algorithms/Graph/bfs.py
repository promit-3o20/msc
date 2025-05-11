class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0

    def show(self):
        return self.items

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)  # comment this line for directed graph

    def bfs(self, start):
        visited = []
        q = Queue()
        q.enqueue(start)
        visited.append(start)

        print(f"\nBFS traversal starting from node {start}:")

        while not q.is_empty():
            current = q.dequeue()
            print(current, end=" ")

            for neighbor in self.adj_list.get(current, []):
                if neighbor not in visited:
                    visited.append(neighbor)
                    q.enqueue(neighbor)
        print("\nVisited Nodes:", visited)

    def show_graph(self):
        print("\nAdjacency List of the Graph:")
        for node in self.adj_list:
            print(f"{node} -> {self.adj_list[node]}")

def main():
    graph = Graph()
    print("==== Breadth-First Search (BFS) ====")
    
    num_edges = int(input("Enter number of edges: "))
    print("Enter edges (format: node1 node2):")
    for _ in range(num_edges):
        u, v = input().split()
        graph.add_edge(u, v)

    graph.show_graph()

    while True:
        start_node = input("\nEnter starting node for BFS: ")
        if start_node not in graph.adj_list:
            print("Node not in graph. Try again.")
        else:
            break

    graph.bfs(start_node)

if __name__ == "__main__":
    main()
