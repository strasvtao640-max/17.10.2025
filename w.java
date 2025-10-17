import java.util.*;


class TSP {
    private int[][] graph;
    private int n;
    private int minCost;
    private List<Integer> bestPath;

    public TSP(int[][] matrix) {
        this.graph = matrix;
        this.n = matrix.length;
        this.minCost = Integer.MAX_VALUE;
        this.bestPath = new ArrayList<>();
    }

    public void solve() {
        // Создаем список вершин (кроме начальной)
        List<Integer> vertices = new ArrayList<>();
        for (int i = 1; i < n; i++) {
            vertices.add(i);
        }

        // Начинаем с вершины 0
        List<Integer> currentPath = new ArrayList<>();
        currentPath.add(0);

        minCost = Integer.MAX_VALUE;
        bestPath.clear();

        // Запускаем рекурсивный поиск
        solveRecursive(vertices, currentPath, 0);
    }

    private void solveRecursive(List<Integer> remaining, List<Integer> currentPath, int currentCost) {
        // Базовый случай: все вершины посещены
        if (remaining.isEmpty()) {
            // Добавляем путь обратно к начальной вершине
            int totalCost = currentCost + graph[currentPath.get(currentPath.size() - 1)][0];
            
            if (totalCost < minCost) {
                minCost = totalCost;
                bestPath = new ArrayList<>(currentPath);
                bestPath.add(0); // Добавляем возврат к началу
            }
            return;
        }

        // Рекурсивный случай: пробуем все возможные следующие вершины
        for (int i = 0; i < remaining.size(); i++) {
            int nextVertex = remaining.get(i);
            int lastVertex = currentPath.get(currentPath.size() - 1);
            
            // Вычисляем новую стоимость
            int newCost = currentCost + graph[lastVertex][nextVertex];
            
            // Если текущая стоимость уже превышает минимум, пропускаем
            if (newCost >= minCost) {
                continue;
            }

            // Обновляем списки для рекурсивного вызова
            List<Integer> newRemaining = new ArrayList<>(remaining);
            newRemaining.remove(i);
            
            List<Integer> newPath = new ArrayList<>(currentPath);
            newPath.add(nextVertex);

            solveRecursive(newRemaining, newPath, newCost);
        }
    }

    public void printSolution() {
        System.out.println("Минимальная стоимость пути: " + minCost);
        System.out.print("Оптимальный маршрут: ");
        for (int i = 0; i < bestPath.size(); i++) {
            System.out.print(bestPath.get(i));
            if (i < bestPath.size() - 1) {
                System.out.print(" -> ");
            }
        }
        System.out.println();
    }

    public static void main(String[] args) {
        // Пример графа (матрица смежности)
        int[][] graph = {
            {0, 10, 15, 20},
            {10, 0, 35, 25},
            {15, 35, 0, 30},
            {20, 25, 30, 0}
        };

        TSP tsp = new TSP(graph);
        tsp.solve();
        tsp.printSolution();
    }
}