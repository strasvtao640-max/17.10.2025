#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

bool is_palindrome(int number) {
    // Преобразуем число в строку
    string num_str = to_string(number);
    
    // Создаем копию строки и разворачиваем её
    string reversed_str = num_str;
    reverse(reversed_str.begin(), reversed_str.end());
    
    // Сравниваем исходную строку с развернутой
    return num_str == reversed_str;
}

int main() {
    int number;
    
    cout << "Enter a positive number: ";
    cin >> number;
    
    // Проверка на положительное число
    if (number < 0) {
        cout << "Error: Please enter a positive number!" << endl;
        return 1;
    }
    
    // Проверяем, является ли число палиндромом
    if (is_palindrome(number)) {
        cout << "The number " << number << " is a palindrome!" << endl;
    } else {
        cout << "The number " << number << " is not a palindrome!" << endl;
    }
    
    return 0;
}