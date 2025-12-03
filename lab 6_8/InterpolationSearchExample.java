public class InterpolationSearchExample {

    public static int interpolationSearch(int[] arr, int x) {
        int lo = 0;
        int hi = arr.length - 1;

        while (lo <= hi && x >= arr[lo] && x <= arr[hi]) {
            if (arr[hi] == arr[lo]) {
                if (arr[lo] == x) return lo;
                else return -1;
            }

            int pos = lo + (int)((long)(hi - lo) * (x - arr[lo]) / (arr[hi] - arr[lo]));

            if (arr[pos] == x) {
                return pos;
            } else if (arr[pos] < x) {
                lo = pos + 1;
            } else {
                hi = pos - 1;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] arr = {10, 20, 30, 40, 50, 60, 70};
        int target = 40;

        int result = interpolationSearch(arr, target);

        System.out.print("Массив: ");
        for (int v : arr) System.out.print(v + " ");
        System.out.println("\nИщем элемент: " + target);

        if (result != -1) {
            System.out.println("Элемент найден на позиции (индекс): " + result);
        } else {
            System.out.println("Элемент не найден");
        }
    }
}
