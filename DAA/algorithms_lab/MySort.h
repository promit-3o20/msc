#ifndef MySort_H
#define MySort_H

#include <iostream>

using namespace std;

class MySort
{
public:
    static int quickPartition(int arr[], int low, int high)
    {
        int pivot = arr[high];
        int i, j;
        i = low - 1;
        for (j = low; j <= high - 1; j++)
        {
            if (arr[j] <= pivot)
            {
                i++;
                swap(arr[i], arr[j]);
            }
        }
        swap(arr[i + 1], arr[high]);
        return i + 1;
    }

    static void quickSort(int arr[], int low, int high)
    {
        if (low < high)
        {
            int q = quickPartition(arr, low, high);
            quickSort(arr, low, q - 1);
            quickSort(arr, q + 1, high);
        }
    }
};

#endif