class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def get_node_value(head, index, counter=0):
  if head is None or index < 0:
    # return the value of that head 
    return None 
  elif counter == index:
    # return the head value at that index
    return head.val
  else:
    return get_node_value(head.next, index, counter+1)
  
if __name__ == "__main__":
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.next = b
    b.next = c
    c.next = d

    # a -> b -> c -> d

    print(get_node_value(a, 2)) # 'c'

    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.next = b
    b.next = c
    c.next = d

    # a -> b -> c -> d

    print(get_node_value(a, 3)) # 'd'

    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.next = b
    b.next = c
    c.next = d

    # a -> b -> c -> d

    print(get_node_value(a, 7)) # None