#include <iostream>
#include "MyArray.h"
#include "MySort.h"

using namespace std;

int main()
{

    int arr_size;
    cout << "Enter the size of the array: ";
    cin >> arr_size;
    int arr[arr_size];

    MyArray::arrInput(arr_size, arr);
    MyArray::arrOutput(arr_size, arr);
    cout << "After sorting the array by QUICK SORT\n";
    MySort::quickSort(arr, 0, arr_size-1);
    MyArray::arrOutput(arr_size, arr);

    return 0;
}
