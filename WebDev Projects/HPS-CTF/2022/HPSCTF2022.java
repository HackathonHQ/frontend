public class HPSCTF2022 {

  //Represents the node of list.
  public class Node {

    int data;
    Node next;

    public Node(int data) {
      this.data = data;
    }
  }

  //Declaring head and tail pointer as null.
  public Node head = null;
  public Node tail = null;

  //This function will add the new node at the end of the list.
  public void add(int data) {
    //Create new node
    Node newNode = new Node(data);
    //Checks if the list is empty.
    if (head == null) {
      //If list is empty, both head and tail would point to new node.
      head = newNode;
      tail = newNode;
      newNode.next = head;
    } else {
      //tail will point to new node.
      tail.next = newNode;
      //New node will become new tail.
      tail = newNode;
      //Since, it is circular linked list tail will point to head.
      tail.next = head;
    }
  }

  //Displays all the nodes in the list
  public void display() {
    Node current = head;
    if (head == null) {
      print("List is empty");
    } else {
      print("Nodes of the circular linked list: ");
      do {
        //Prints each node by incrementing pointer.
        System.out.print(" " + current.data);
        current = current.next;
      } while (current != head);
    //   print();
    }
  }

  public void print(String x) {
      System.out.println();
  }

  public void print(StringBuffer modnode) {
      // attached the tailend into the modified node
      StringBuffer tailend=modnode;
    for(int i =0;i<modnode.length();i++){
        // appends the circular linked list by decrementing point
        modnode.append(tailend.charAt(modnode.length()-i-1));
    }
    // reverse the node
    modnode.reverse();
    for(int i =1;i<=modnode.length();i++){
        // appends the circular linked list by incrementing point
        modnode.append(tailend.charAt(modnode.length()-i));
    }
    System.out.println(modnode);
}
  public static void main(String[] args) {
    HPSCTF2022 cl = new HPSCTF2022();
    StringBuffer sb = new StringBuffer("⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛");
    // the flag was once in the place of the black boxes
    cl.print(sb);
    //Adds data to the list
    cl.add(1);
    cl.add(2);
    cl.add(3);
    cl.add(4);
    //Displays all the nodes present in the list
    cl.display();
  }
}
