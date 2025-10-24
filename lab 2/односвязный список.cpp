#include <iostream>
using namespace std;

// Структура узла списка
struct ListNode {
    int value;
    ListNode* next;
    
    ListNode(int val) : value(val), next(nullptr) {}
};

// Создание списка с использованием цикла вместо рекурсии
ListNode* createList(int n) {
    if (n <= 0) return nullptr;
    
    cout << "Enter value: ";
    int value;
    cin >> value;
    
    ListNode* head = new ListNode(value);
    ListNode* current = head;
    
    for (int i = 1; i < n; i++) {
        cout << "Enter value: ";
        cin >> value;
        current->next = new ListNode(value);
        current = current->next;
    }
    
    return head;
}

// Вывод списка
void printList(ListNode* head) {
    ListNode* current = head;
    while (current != nullptr) {
        cout << current->value;
        if (current->next != nullptr) {
            cout << " -> ";
        }
        current = current->next;
    }
    cout << " -> NULL" << endl;
}

// Вставка элемента в начало
void insertFront(ListNode** head, int value) {
    ListNode* newNode = new ListNode(value);
    newNode->next = *head;
    *head = newNode;
}

// Удаление элемента
bool deleteElement(ListNode** head, int value) {
    if (*head == nullptr) return false;
    
    // Если удаляемый элемент первый
    if ((*head)->value == value) {
        ListNode* temp = *head;
        *head = (*head)->next;
        delete temp;
        return true;
    }
    
    // Поиск элемента для удаления
    ListNode* current = *head;
    while (current->next != nullptr && current->next->value != value) {
        current = current->next;
    }
    
    if (current->next != nullptr) {
        ListNode* temp = current->next;
        current->next = current->next->next;
        delete temp;
        return true;
    }
    
    return false;
}

// Поиск элемента
bool searchElement(ListNode* head, int value) {
    ListNode* current = head;
    while (current != nullptr) {
        if (current->value == value) {
            return true;
        }
        current = current->next;
    }
    return false;
}

// Удаление всего списка
void deleteList(ListNode** head) {
    while (*head != nullptr) {
        ListNode* temp = *head;
        *head = (*head)->next;
        delete temp;
    }
}

int main() {
    ListNode* head = nullptr;
    int n;
    
    cout << "Enter number of elements: ";
    cin >> n;
    
    // Создание списка
    head = createList(n);
    cout << "Created list: ";
    printList(head);
    
    // Вставка в начало
    insertFront(&head, 999);
    cout << "After inserting 999 at the beginning: ";
    printList(head);
    
    // Поиск элемента
    int searchVal;
    cout << "Enter number for searching: ";
    cin >> searchVal;
    if (searchElement(head, searchVal)) {
        cout << "Element " << searchVal << " found" << endl;
    } else {
        cout << "Element " << searchVal << " not found" << endl;
    }
    
    // Удаление элемента
    int deleteVal;
    cout << "Enter number for deleting: ";
    cin >> deleteVal;
    if (deleteElement(&head, deleteVal)) {
        cout << "Element deleted. New list: ";
        printList(head);
    } else {
        cout << "Element not found" << endl;
    }
    
    // Удаление всего списка
    deleteList(&head);
    cout << "List deleted. Head = " << head << endl;
    
    return 0;
}