#include <iostream>
#include <unistd.h>
#include "MyArray.h" //myhead

using namespace std;

int binarySearch(int arr[], int low, int high, int x)
{
    if (low <= high)
    {
        int mid = low + (high - low) / 2;
        if (arr[mid] == x)
        {
            return mid;
        }
        else if (arr[mid] > x)
        {
            return binarySearch(arr, 0, mid - 1, x);
        }
        else
        {
            return binarySearch(arr, mid + 1, high, x);
        }
    }
    return -1;
}

int main(void)
{
    int arr_size;
    cout << "Size of an array: ";
    cin >> arr_size;

    int arr[arr_size];

    MyArray::arrInput(arr_size, arr);
    MyArray::arrOutput(arr_size, arr);

    MyArray isSort;
    if (isSort.MyArray::isSortedAscending(arr_size, arr))
    {
        cout << "Already Sorted.\n";
    }
    else
    {
        cout << "Sorting......\n";
        sleep(1);
        MyArray ::arrAscendingSort(arr_size, arr);
        cout << "Sorted.\n";
    }
    MyArray::arrOutput(arr_size, arr);
    int x;
    cout << "Enter the element which you want to find: ";
    cin >> x;
    int result = binarySearch(arr, 0, arr_size - 1, x);
    if (result == -1)
        cout << "Element not present in array." << endl;
    else
        cout << "Element found at index " << result << endl;
    return 0;
}