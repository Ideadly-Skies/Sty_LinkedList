class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

if __name__ == "__main__":
    # create new node with different values 
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')

    # build the linkedlist
    a.next = b
    b.next = c
    c.next = d

    # A -> B -> C -> D (iteratively)
    def print_list(head: Node):
        """
        print the current LinkedList starting from the head pointer 
        """
        # set current as head
        current = head
        
        while (current is not None):
            # print the current node value  
            print(current.val)
            current = current.next
    
    # A -> B -> C -> D (recursively)
    def print_list_recursive(head: Node):
        """
        print the current LinkedList recursively 
        """
        if head is None:
            return
        print(head.val)
        print_list_recursive(head.next)

    # print the list
    print_list(a)