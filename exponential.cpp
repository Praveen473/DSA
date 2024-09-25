#include <iostream>
using namespace std;

int binarySearch(int arr[], int low, int high, int key) {
    while (low <= high) {
        int mid = low + (high - low) / 2;

        if (arr[mid] == key)
            return mid;

        if (arr[mid] < key)
            low = mid + 1;
        else
            high = mid - 1;
    }
    return -1;
}

int exponentialSearch(int arr[], int n, int key) {
    if (arr[0] == key)
        return 0;

    int i = 1;
    while (i < n && arr[i] <= key)
        i = i * 2;
        cout<<i;

    return binarySearch(arr, i / 2, min(i, n - 1), key);
}

int main() {
    int arr[] = {100,120,150,170,200,220,240};
    int n = sizeof(arr) / sizeof(arr[0]);
    int key = 170;

    int index = exponentialSearch(arr, n, key);

    if (index != -1)
        cout << "Element found at index " << index << endl;
    else
        cout << "Element not found." << endl;

    return 0;
}
