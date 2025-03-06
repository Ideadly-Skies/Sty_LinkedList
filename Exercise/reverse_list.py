class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def reverse_list(head, prev=None, curr=None, next=None):
    if (not curr):
        # init variables
        curr = head
        next = head.next
        
        # return sole variable 
        if (next is None): return curr
    
    elif (curr.next is None):
        # set next node of current node to prev
        curr.next = prev
        return curr
    
    # set current pointer's next to prev
    curr.next = prev

    # recurse to the end of the list
    return reverse_list(head, curr, next, next.next)

if __name__ == "__main__":
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    # a -> b -> c -> d -> e -> f

    node = reverse_list(a) # f -> e -> d -> c -> b -> a

    while (node != None):
       print(node.val)
       node = node.next