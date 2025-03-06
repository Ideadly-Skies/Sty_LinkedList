class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def create_linked_list(values, tail=None, head=None, first=True):
    if values == []:
        # base case
        if first:
           return None
        else:
           return head
    elif first:
       # init pointers to store node values
       head = Node(values[0])
       tail = head
       first = False # node is visited 
    else:
       # set new node to a new node with the first value of the
       # new list 
       new_node = Node(values[0])
       tail.next = new_node
       tail = tail.next

    # recursive case
    return create_linked_list(values[1:],tail,head,first) 

if __name__ == "__main__":
    head = create_linked_list(["h", "e", "y"])
    head = create_linked_list([1, 7, 1, 8])
    head = create_linked_list(["a"])
    head = create_linked_list([])

    while (head is not None):
       print(head.val)
       head = head.next
