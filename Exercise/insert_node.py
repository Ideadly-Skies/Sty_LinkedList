class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def insert_node(head, value, index, prev=None, curr=None, counter=1):
    if (curr is None):
       # insert item at last position
        if counter > 1:
            new_node = Node(value)
            prev.next = new_node
            return head 
        else:
            # init pointer
            curr = head.next
            prev = head
    elif (index == 0):
       # insert new_node to linked-list
       new_node = Node(value)
       new_node.next = prev
       return new_node 
    elif (prev.next is None):
       # insert at last position
       new_node = Node(value)
       prev.next = new_node 
       return head
    elif (counter == index):
        # insert in between two nodes
        new_node = Node(value)
        new_node.next = curr 
        prev.next = new_node
        return head 
    else:
        # increment pointers forward
        prev = prev.next
        curr = curr.next
        counter += 1
    
    return insert_node(head, value, index, prev, curr, counter)

if __name__ == "__main__":
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.next = b
    b.next = c
    c.next = d

    # a -> b -> c -> d

    node = insert_node(a, 'm', 4)
    # a -> b -> c -> d -> m

    while (node is not None):
       print(node.val)
       node = node.next