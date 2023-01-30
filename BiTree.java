/**
 * 1. Хэш функция это функция, которая преобразовывает входные данные произвольной длины в выходные данные
 * фиксированной длины (выходную битовую строку установленной длины), выполняемое определённым алгоритмом.
 * Одинаковые (эквивалентные) входные данные иммеют одинаковые (эквивалентные) хэш-функции. В свою очередь,
 * две одинаковые хэш-функции не говорят о том, что они образованны из одинаковых входных данных, это
 * свидетельствует о коллизии.
 */


/**
 * 2. Обходы бинарного дерева
 */
public class BiTree {

    public static void main(String[] args) {
        // Node tree = buildTree(19);
        Node root = new Node(2);
        Node l1 = new Node(21);
        Node r1 = new Node(31);
        Node l1l1 = new Node(221);
        Node l1r1 = new Node(331);
        Node r1l1 = new Node (431);
        Node r1l1l1 = new Node(6431);
         

        root.left = l1;
        root.right = r1;
        l1.left = l1l1;
        l1.right = l1r1;
        r1.left = r1l1;
        r1l1.left = r1l1l1;
        r1l1l1.left = new Node(86431);
        r1l1.right = new Node(7431);
        root.value = 1;



        // PreOrderPrint(tree, "");
        System.out.println();
        System.out.println("Pre-order format of the bi-tree: ");
        PreOrderPrint(root, "");
        System.out.println();
        System.out.println("In-order format of the bi-tree: ");
        InOrderPrint(root, "");
        System.out.println();
        System.out.println("Reverse In-order format of the bi-tree: ");
        ReverseInOrderPrint(root, "");
        System.out.println();
        System.out.println("Post-order format of the bi-tree: ");
        PostOrderPrint(root, "");
    }

    public static void PreOrderPrint(Node root, String sp) {
        if (root != null) {
            System.out.println(sp + root.value);
            PreOrderPrint(root.left, sp + "|  ");
            PreOrderPrint(root.right, sp + "   ");
        }
    }

    public static void InOrderPrint(Node root, String sp) {
        if (root != null) {
            InOrderPrint(root.left, sp + "|  ");
            System.out.println(sp + root.value);
            InOrderPrint(root.right, sp + "   ");
        }
    }

    public static void PostOrderPrint(Node root, String sp) {
        if (root != null) {
            PostOrderPrint(root.left, sp + "|  ");
            PostOrderPrint(root.right, sp + "   ");
            System.out.println(sp + root.value);
        }
    }

    public static void ReverseInOrderPrint(Node root, String sp) {
        if (root != null) {
            ReverseInOrderPrint(root.right, sp + "|  ");
            System.out.println(sp + root.value);
            ReverseInOrderPrint(root.left, sp + "   ");
        }
    }

    static int t = 0;

    public static Node buildTree(int n) {
        Node root;
        if (n == 0)
            return null;
        else {
            root = new Node(t++);
            root.left = buildTree(n / 2);
            root.right = buildTree(n - n / 2 - 1);
        }
        return root;
    }

    public static class Node {

        Node left;
        Node right;
        int value;

        public Node(int value) {
            this.value = value;
        }
    }
}
