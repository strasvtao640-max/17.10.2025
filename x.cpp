#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

class TSP {
private:
    vector<vector<int>> graph;
    int n;

public:
    TSP(vector<vector<int>> matrix) {
        graph = matrix;
        n = matrix.size();
    }

    int solve() {
        // перестановка начальная: 0, 1, 2, ..., n-1
        vector<int> vertex;
        for (int i = 0; i < n; i++) {
            vertex.push_back(i);
        }

        int min_path = INT_MAX;

        //все возможные перестановки вершин
        do {
            int current_pathweight = 0;

            // Вычисляем стоимость текущего пути
            for (int i = 0; i < n - 1; i++) {
                current_pathweight += graph[vertex[i]][vertex[i + 1]];
            }
            // Добавляем путь обратно к начальной вершине
            current_pathweight += graph[vertex[n - 1]][vertex[0]];

            // Обновляем минимальную стоимость
            min_path = min(min_path, current_pathweight);

        } while (next_permutation(vertex.begin() + 1, vertex.end()));

        return min_path;
    }

    void printSolution() {
        int min_cost = solve();
        cout << "Минимальная стоимость пути коммивояжера: " << min_cost << endl;
    }
};

int main() {
    // Пример графа (матрица смежности)
    vector<vector<int>> graph = {
        {0, 10, 15, 20},
        {10, 0, 35, 25},
        {15, 35, 0, 30},
        {20, 25, 30, 0}
    };

    TSP tsp(graph);
    tsp.printSolution();

    return 0;
}