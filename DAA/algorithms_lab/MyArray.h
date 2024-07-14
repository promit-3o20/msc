#ifndef MyArray_H
#define MyArray_H

#include <iostream>
using namespace std;

class MyArray
{
public:
    static void arrInput(int arr_size, int arr[])
    {
        // cout << "Enter the elements : ";
        for (int i = 0; i < arr_size; i++)
        {
            cout << "Enter the element " << i << ": ";
            cin >> arr[i];
        }
    }

    static void arrOutput(int arr_size, int arr[])
    {
        cout << "The array elements are: ";
        for (int i = 0; i < arr_size; i++)
        {
            cout << arr[i] << " ";
        }
        cout << endl;
    }

    static void arrAscendingSort(int arr_size, int arr[])
    {
        for (int i = 0; i < arr_size - 1; i++)
        {
            for (int j = 0; j < arr_size - i - 1; j++)
            {
                if (arr[j] > arr[j + 1])
                {
                    // Swap arr[j] and arr[j + 1]
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }

    static void arrDescendingSort(int arr_size, int arr[])
    {
        for (int i = 0; i < arr_size - 1; i++)
        {
            for (int j = 0; j < arr_size - i - 1; j++)
            {
                if (arr[j] < arr[j + 1])
                {
                    // Swap arr[j] and arr[j + 1]
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }

    bool isSortedAscending(int arr_size, int arr[])
    {
        for (int i = 0; i < arr_size - 1; i++)
        {
            if (arr[i] > arr[i + 1])
            {
                return false;
            }
        }
        return true;
    }

    bool isSortedDescending(int arr_size, int arr[])
    {
        for (int i = 0; i < arr_size - 1; i++)
        {
            if (arr[i] < arr[i + 1])
            {
                return false;
            }
        }
        return true;
    }
};
#endif