class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def remove_node(head, target_val, prev=None, curr=None, next=None, isFirst=True):
    # init pointer 
    if isFirst:
        curr = head
        next = curr.next
        isFirst = False
    
    # remove current_node 
    if curr.val == target_val:
        if prev is None:
            return head.next
        
        # set prev.next to next 
        prev.next = next
        
        # clean up curr pointer 
        curr = None
        
        # return head 
        return head 
         
    # recursive case
    return remove_node(head, target_val, curr, next, next.next, isFirst) 
         
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

    curr = remove_node(a, "c")
    # a -> b -> d -> e -> f

    while curr.next is not None:
        print(curr.val, end=" -> ")
        curr = curr.next
    print(curr.val, end=" ")
    print("") 
    
    x = Node("x")
    y = Node("y")
    z = Node("z")

    x.next = y
    y.next = z

    # x -> y -> z

    curr = remove_node(x, "z")
    # x -> y
    
    while curr.next is not None:
        print(curr.val, end=" -> ")
        curr = curr.next
    print(curr.val, end=" ")
    print("")  