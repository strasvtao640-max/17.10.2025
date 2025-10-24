import java.util.Scanner;

class Node {
    int data;
    Node next;
    
    Node(int data) {
        this.data = data;
        this.next = null;
    }
}

public class LinkedList {
    private Node head;
    private Scanner scanner;
    
    public LinkedList() {
        head = null;
        scanner = new Scanner(System.in);
    }
    
    // Создание списка с использованием цикла
    public void createList(int n) {
        if (n <= 0) return;
        
        System.out.print("Введите значение: ");
        head = new Node(scanner.nextInt());
        
        Node current = head;
        for (int i = 1; i < n; i++) {
            System.out.print("Введите значение: ");
            current.next = new Node(scanner.nextInt());
            current = current.next;
        }
    }
    
    // Вывод списка
    public void printList() {
        Node current = head;
        while (current != null) {
            System.out.print(current.data);
            if (current.next != null) {
                System.out.print(" -> ");
            }
            current = current.next;
        }
        System.out.println(" -> NULL");
    }
    
    // Вставка в начало
    public void insertFront(int value) {
        Node newNode = new Node(value);
        newNode.next = head;
        head = newNode;
    }
    
    // Удаление элемента
    public boolean deleteElement(int value) {
        if (head == null) return false;
        
        if (head.data == value) {
            head = head.next;
            return true;
        }
        
        Node current = head;
        while (current.next != null && current.next.data != value) {
            current = current.next;
        }
        
        if (current.next != null) {
            current.next = current.next.next;
            return true;
        }
        return false;
    }
    
    // Поиск элемента
    public boolean searchElement(int value) {
        Node current = head;
        while (current != null) {
            if (current.data == value) {
                return true;
            }
            current = current.next;
        }
        return false;
    }
    
    // Удаление всего списка
    public void deleteList() {
        head = null;
    }
    
    public static void main(String[] args) {
        LinkedList list = new LinkedList();
        Scanner mainScanner = new Scanner(System.in);
        
        System.out.print("Введите количество элементов: ");
        int n = mainScanner.nextInt();
        
        // Создание списка
        list.createList(n);
        System.out.print("Созданный список: ");
        list.printList();
        
        // Вставка в начало
        list.insertFront(999);
        System.out.print("После вставки 999 в начало: ");
        list.printList();
        
        // Поиск элемента
        System.out.print("Введите значение для поиска: ");
        int searchVal = mainScanner.nextInt();
        if (list.searchElement(searchVal)) {
            System.out.println("Элемент " + searchVal + " найден");
        } else {
            System.out.println("Элемент " + searchVal + " не найден");
        }
        
        // Удаление элемента
        System.out.print("Введите значение для удаления: ");
        int deleteVal = mainScanner.nextInt();
        if (list.deleteElement(deleteVal)) {
            System.out.print("Элемент удален. Новый список: ");
            list.printList();
        } else {
            System.out.println("Элемент не найден");
        }
        
        mainScanner.close();
    }
}