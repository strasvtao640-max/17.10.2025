import java.util.*;

// Пример собственного представления дерева (общее дерево, не обязательно бинарное)
class TreeNode {
    String value;
    List<TreeNode> children = new ArrayList<>();

    TreeNode(String value) {
        this.value = value;
    }

    void addChild(TreeNode child) {
        children.add(child);
    }
}

// Пример собственного представления графа (неориентированный граф, список смежности)
class Graph {
    private final Map<String, List<String>> adj = new HashMap<>();

    public void addVertex(String v) {
        adj.putIfAbsent(v, new ArrayList<>());
    }

    public void addEdge(String v1, String v2) {
        addVertex(v1);
        addVertex(v2);
        adj.get(v1).add(v2);
        adj.get(v2).add(v1); // неориентированный граф
    }

    // простой обход в ширину
    public List<String> bfs(String start) {
        List<String> order = new ArrayList<>();
        if (!adj.containsKey(start)) return order;
        Set<String> visited = new HashSet<>();
        Queue<String> queue = new ArrayDeque<>();
        visited.add(start);
        queue.add(start);
        while (!queue.isEmpty()) {
            String v = queue.remove();
            order.add(v);
            for (String neighbor : adj.get(v)) {
                if (!visited.contains(neighbor)) {
                    visited.add(neighbor);
                    queue.add(neighbor);
                }
            }
        }
        return order;
    }
}

public class Main {
    // печать дерева с отступами
    public static void printTree(TreeNode node, int level) {
        if (node == null) return;
        for (int i = 0; i < level; i++) {
            System.out.print("  ");
        }
        System.out.println(node.value);
        for (TreeNode child : node.children) {
            printTree(child, level + 1);
        }
    }

    public static void main(String[] args) {
        // ---------- Пример дерева: структура меню веб-сайта ----------
        TreeNode root = new TreeNode("Главная страница");
        TreeNode products = new TreeNode("Каталог товаров");
        TreeNode about = new TreeNode("О компании");
        TreeNode contact = new TreeNode("Контакты");

        root.addChild(products);
        root.addChild(about);
        root.addChild(contact);

        TreeNode electronics = new TreeNode("Электроника");
        TreeNode clothes = new TreeNode("Одежда");
        products.addChild(electronics);
        products.addChild(clothes);

        System.out.println("Структура меню (дерево):");
        printTree(root, 0);

        // ---------- Пример графа: дружеские связи пользователей ----------
        Graph social = new Graph();
        social.addEdge("Антон", "Борис");
        social.addEdge("Антон", "Дима");
        social.addEdge("Борис", "Егор");
        social.addEdge("Дима", "Егор");
        social.addEdge("Егор", "Инна");

        System.out.println();
        System.out.println("Обход графа дружбы из вершины 'Антон':");
        System.out.println(social.bfs("Антон"));
    }
}