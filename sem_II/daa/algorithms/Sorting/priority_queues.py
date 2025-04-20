class PriorityQueue:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def max_heapify(self, i):
        largest = i
        l = self.left(i)
        r = self.right(i)
        n = len(self.heap)

        if l < n and self.heap[l] > self.heap[largest]:
            largest = l
        if r < n and self.heap[r] > self.heap[largest]:
            largest = r

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.max_heapify(largest)

    def heap_maximum(self):
        if len(self.heap) < 1:
            return "Heap is empty."
        return self.heap[0]

    def heap_extract_max(self):
        if len(self.heap) < 1:
            return "Heap underflow."

        max_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.max_heapify(0)
        return max_val

    def heap_increase_key(self, i, key):
        if key < self.heap[i]:
            return f"New element ({key}) is smaller than current key ({self.heap[i]})."

        self.heap[i] = key
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)
        return "Key increased successfully."

    def max_heap_insert(self, key):
        self.heap.append(float('-inf'))
        self.heap_increase_key(len(self.heap) - 1, key)

    def display(self):
        print("Current Heap:", self.heap)


# ---------- USER INTERACTION ----------
def main():
    heap = PriorityQueue()

    while True:
        print("\n--- Priority Queue Operations ---")
        print("1. Insert key (space-separated)")
        print("2. Get maximum")
        print("3. Extract maximum")
        print("4. Increase a key")
        print("5. Display Heap")
        print("0. Exit")

        choice = input("Enter your choice (0-5): ")

        if choice == '1':
            keys = input("Enter keys to insert (space separated): ")
            try:
                key_list = list(map(int, keys.strip().split()))
                for key in key_list:
                    heap.max_heap_insert(key)
                print(f"{len(key_list)} keys inserted successfully.")
            except ValueError:
                print("Invalid input. Please enter space-separated integers.")
        elif choice == '2':
            print("Maximum value:", heap.heap_maximum())
        elif choice == '3':
            print("Extracted maximum:", heap.heap_extract_max())
        elif choice == '4':
            index = int(input("Enter index to increase key: "))
            if index < 0 or index >= len(heap.heap):
                print("Invalid index.")
                continue
            new_key = int(input("Enter new key value: "))
            print(heap.heap_increase_key(index, new_key))
        elif choice == '5':
            heap.display()
        elif choice == '0':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please enter between 0-5.")

if __name__ == "__main__":
    main()

