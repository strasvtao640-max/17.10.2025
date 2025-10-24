#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    // Исходный массив цифр от 1 до 10 в произвольном порядке
    vector<int> numbers = {2, 1, 3, 9, 5, 6, 8, 7, 4, 10};

    // Используем алгоритм partition для разделения чисел
    vector<int> list1, list2;
    
    // Копируем числа 1-5 в первый список
    copy_if(numbers.begin(), numbers.end(), back_inserter(list1),
            [](int num) { return num <= 5; });
    
    // Копируем числа 6-10 во второй список
    copy_if(numbers.begin(), numbers.end(), back_inserter(list2),
            [](int num) { return num > 5; });

    // Выводим результаты
    cout << "First list (1-5): ";
    for (int num : list1) {
        cout << num << " ";
    }
    cout << endl;

    cout << "Second list (6-10): ";
    for (int num : list2) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}