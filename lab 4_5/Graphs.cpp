#include <iostream>
#include <vector>
#include <queue>
#include <string>

// Собственное представление общего дерева (каждый узел может иметь несколько детей)
struct TreeNode {
    std::string value;
    std::vector<TreeNode*> children;

    explicit TreeNode(const std::string& v) : value(v) {}
};

void printTree(TreeNode* node, int level = 0) {
    if (!node) return;
    for (int i = 0; i < level; ++i) std::cout << "  ";
    std::cout << node->value << "\n";
    for (TreeNode* child : node->children) {
        printTree(child, level + 1);
    }
}

void deleteTree(TreeNode* node) {
    if (!node) return;
    for (TreeNode* child : node->children) {
        deleteTree(child);
    }
    delete node;
}

// Собственное представление неориентированного графа (список смежности)
class Graph {
public:
    explicit Graph(int vertices) : adj(vertices) {}

    void addEdge(int u, int v) {
        // неориентированный граф
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    void bfs(int start) const {
        std::vector<bool> visited(adj.size(), false);
        std::queue<int> q;
        visited[start] = true;
        q.push(start);
        std::cout << "BFS order from vertex " << start << ": ";
        while (!q.empty()) {
            int v = q.front();
            q.pop();
            std::cout << v << ' ';
            for (int neighbor : adj[v]) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    q.push(neighbor);
                }
            }
        }
        std::cout << "\n";
    }

private:
    std::vector<std::vector<int>> adj;
};

int main() {
    // -------- Пример дерева: структура отделов компании --------
    TreeNode* ceo = new TreeNode("CEO");
    TreeNode* sales = new TreeNode("Sales department");
    TreeNode* it = new TreeNode("IT department");
    TreeNode* hr = new TreeNode("HR");

    ceo->children.push_back(sales);
    ceo->children.push_back(it);
    ceo->children.push_back(hr);

    TreeNode* backend = new TreeNode("Backend team");
    TreeNode* frontend = new TreeNode("Frontend team");
    it->children.push_back(backend);
    it->children.push_back(frontend);

    std::cout << "Company structure (tree):\n";
    printTree(ceo);

    // -------- Пример графа: схема дорог между городами --------
    Graph g(5); // вершины 0..4
    g.addEdge(0, 1); // 0-1
    g.addEdge(0, 2); // 0-2
    g.addEdge(1, 3); // 1-3
    g.addEdge(2, 3); // 2-3
    g.addEdge(3, 4); // 3-4

    std::cout << "\nRoad network (graph):\n";
    g.bfs(0);

    // очистка памяти
    deleteTree(ceo);

    return 0;
}