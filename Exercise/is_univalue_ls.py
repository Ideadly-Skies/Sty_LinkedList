class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def is_univalue_list(head, val=0, start=True):
    # base case reached 
    if head.next == None:
        # sole node are unique!
        if start:
           return True

        # not sole node 
        if head.val != val:
           return False
        else: 
           return True 
    
    # start of linkedlist
    if start:
       # skip over this node
       start = False 
    else:
        # not a univalue list
        if head.val != val:
            return False
    return is_univalue_list(head.next, head.val, False)

if __name__ == "__main__":
    a = Node(7)
    b = Node(7)
    c = Node(7)

    a.next = b
    b.next = c

    # 7 -> 7 -> 7

    print(is_univalue_list(a)) # True

    a = Node(7)
    b = Node(7)
    c = Node(4)

    a.next = b
    b.next = c

    # 7 -> 7 -> 4

    print(is_univalue_list(a)) # False

    u = Node(2)
    v = Node(2)
    w = Node(2)
    x = Node(2)
    y = Node(2)

    u.next = v
    v.next = w
    w.next = x
    x.next = y

    # 2 -> 2 -> 2 -> 2 -> 2

    print(is_univalue_list(u)) # True

    u = Node(2)
    v = Node(2)
    w = Node(3)
    x = Node(3)
    y = Node(2)

    u.next = v
    v.next = w
    w.next = x
    x.next = y

    # 2 -> 2 -> 3 -> 3 -> 2

    print(is_univalue_list(u)) # False

    z = Node('z')

    # z

    print(is_univalue_list(z)) # True

    u = Node(2)
    v = Node(1)
    w = Node(2)
    x = Node(2)
    y = Node(2)

    u.next = v
    v.next = w
    w.next = x
    x.next = y

    # 2 -> 1 -> 2 -> 2 -> 2

    print(is_univalue_list(u)) # False