package helloapp;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class NumberSplitter {
    public static void main(String[] args) {
        // Исходный массив цифр от 1 до 10
        int[] numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        
        // Используем Stream API для разделения чисел
        List<Integer> list1 = new ArrayList<>();
        List<Integer> list2 = new ArrayList<>();
        
        for (int num : numbers) {
            if (num <= 5) {
                list1.add(num);
            } else {
                list2.add(num);
            }
        }
        
        // Выводим результаты
        System.out.print("Первый список (1-5): ");
        list1.forEach(num -> System.out.print(num + " "));
        System.out.println();
        
        System.out.print("Второй список (6-10): ");
        list2.forEach(num -> System.out.print(num + " "));
        System.out.println();
    }
}
