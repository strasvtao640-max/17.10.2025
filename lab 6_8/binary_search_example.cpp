#include <iostream>
using namespace std;

int binarySearch(int arr[], int n, int target) {
    int left = 0;
    int right = n - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] > target) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    return -1;
}

int main() {
    int arr[] = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19};
    int n = sizeof(arr) / sizeof(arr[0]);
    int target = 7;

    int result = binarySearch(arr, n, target);

    cout << "Массив (отсортированный): ";
    for (int i = 0; i < n; ++i) cout << arr[i] << " ";
    cout << "\nИщем элемент: " << target << endl;

    if (result != -1) {
        cout << "Элемент найден на позиции (индекс): " << result << endl;
    } else {
        cout << "Элемент не найден" << endl;
    }

    return 0;
}
