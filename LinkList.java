
public class LinkList {
    Node head;

    private class Node {
        Node next;
        int value;
    }

    public Node find(int value) {
        Node currentNode = head;
        while (currentNode != null) {
            if (currentNode.value == value) {
                return currentNode;
            }
            currentNode = currentNode.next;
        }
        return null;
    }

    public void addLast(int value) {
        Node currentNode = new Node();
        currentNode.value = value;
        if (head == null) {
            head = currentNode;
        } else {
            Node node = head;
            while (node.next != null) {
                node = node.next;
            }
            node.next = currentNode;
        }
    }

    public void addFirst(int value) {
        Node currentNode = new Node();
        currentNode.value = value;
        if (head == null) {
            head = currentNode;
        } else {
            currentNode.next = head;
            head = currentNode;
        }
    }

    public void print() {
        Node node = head;
        while (node != null) {
            System.out.println(node.value);
            node = node.next;
        }
    }

    // Переворот для односвязного списка
    public void revert() {
        if (head != null && head.next != null) {
            revert(head, head.next);
        }
    }

    private void revert(Node current, Node next) {
        if (next.next != null) {
            revert(next, next.next);
        } else {
            head = next;
        }
        next.next = current;
        current.next = null;
    }

    public static void main(String[] args) {
        LinkList list = new LinkList();
        list.addLast(7);
        list.addLast(6);
        list.addLast(5);
        list.addLast(4);
        list.addLast(3);
        // list.print();
        list.addFirst(8);
        System.out.println("Initial list:");
        list.print();
        System.out.println("Reverted list:");
        list.revert();
        list.print();
    }
}
