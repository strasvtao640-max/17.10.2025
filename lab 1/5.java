package helloapp;
import java.util.Scanner;

public class PalindromeChecker {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Введите положительное число: ");
        int number = scanner.nextInt();
        
        if (number < 0) {
            System.out.println("Ошибка: введите положительное число!");
            return;
        }
        
        boolean isPalindrome = isNumberPalindrome(number);
        
        if (isPalindrome) {
            System.out.println("Число " + number + " является палиндромом!");
        } else {
            System.out.println("Число " + number + " НЕ является палиндромом!");
        }
        
        scanner.close();
    }
    
    // Метод для проверки палиндрома с использованием двух указателей
    public static boolean isNumberPalindrome(int number) {
        String numberStr = String.valueOf(number);
        int left = 0;
        int right = numberStr.length() - 1;
        
        // Сравниваем симметричные позиции
        while (left < right) {
            if (numberStr.charAt(left) != numberStr.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}