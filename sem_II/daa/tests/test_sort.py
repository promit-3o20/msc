import unittest
from lib.MySort import MySort

class TestMySort(unittest.TestCase):
    def setUp(self):
        self.arr = [64, 25, 12, 22, 11]
        self.sorted_arr = [11, 12, 22, 25, 64]

    def test_bubble_sort(self):
        self.assertEqual(MySort.my_bubblesort(self.arr.copy()), self.sorted_arr)
    def test_merge_sort(self):
        self.assertEqual(MySort.my_mergesort(self.arr.copy()), self.sorted_arr)

    def test_quick_sort(self):                                                                                                   
        arr_copy = self.arr.copy()  # Copy to avoid modifying original array
        MySort.my_quicksort(arr_copy, 0, len(arr_copy) - 1)  # In-place QuickSort
        self.assertEqual(arr_copy, self.sorted_arr)
'''
    def test_selection_sort(self):
        self.assertEqual(MySort.selection_sort(self.arr.copy()), self.sorted_arr)

    def test_insertion_sort(self):
        self.assertEqual(MySort.insertion_sort(self.arr.copy()), self.sorted_arr)

    def test_heap_sort(self):
        self.assertEqual(MySort.heap_sort(self.arr.copy()), self.sorted_arr)
'''
if __name__ == "__main__":
    unittest.main()

