class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def reverse_list(head, prev=None, next=None, isFirst=True):
    # base case 
    if next is None and not isFirst:
        head.next = prev
        return head
    
    # init pointers 
    if isFirst:
        # set next pointer to head.next
        next = head.next
        isFirst = False
        
        # sole element
        if next is None:
            return head
    
    # set curr pointer's next to prev 
    head.next = prev
    
    # recursive case   
    return reverse_list(next, head, next.next, isFirst)
    
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

    curr = reverse_list(a) # f -> e -> d -> c -> b -> a
    
    while curr is not None:
        print(curr.val, end=' ')
        curr = curr.next
    print("")