class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
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

    def dfs(self, node, visited, call_stack):
        visited.append(node)
        call_stack.append(node)
        print(f"Visited {node} , Call Stack: {call_stack}")

        for neighbor in self.adj_list[node]:
            if neighbor not in visited:
                self.dfs(neighbor, visited, call_stack)

        call_stack.pop()  # mimic function return (stack pop)

    def start_dfs(self, start_node):
        if start_node not in self.adj_list:
            print("Start node not found in graph.")
            return
        visited = []
        call_stack = []
        print(f"\nDFS Traversal starting from: {start_node}")
        self.dfs(start_node, visited, call_stack)
        print("DFS Complete. Visited nodes:", visited)

    def show_graph(self):
        print("\nGraph (Adjacency List):")
        for node in self.adj_list:
            print(f"{node} -> {self.adj_list[node]}")

def main():
    g = Graph()
    print("==== DFS using with Stack Trace ====")
    num_edges = int(input("Enter number of edges: "))
    print("Enter edges (format: node1 node2):")
    for _ in range(num_edges):
        u, v = input().split()
        g.add_edge(u, v)

    g.show_graph()

    while True:
        start = input("\nEnter starting node for DFS: ")
        if start in g.adj_list:
            break
        print("Node not in graph. Try again.")

    g.start_dfs(start)

if __name__ == "__main__":
    main()
