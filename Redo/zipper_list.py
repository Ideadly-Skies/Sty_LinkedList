class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def zipper_lists(head_1, head_2, tail=None, isFirst=True, count=0, curr1=None, curr2=None):
    # base case 1
    if curr1 is None and not isFirst:
        # make tail point to remainder of curr2 
        tail.next = curr2
        return head_1
    # base case 2 
    if curr2 is None and not isFirst:
        # make tail point to remainder of curr1 
        tail.next = curr1 
        return head_1

    # init tail pointer    
    if isFirst:
       tail = head_1
       curr1 = head_1.next
       curr2 = head_2
       isFirst = False
    else:
        if (count % 2 == 0):
            tail.next = curr1 
            curr1 = curr1.next
        else:
            tail.next = curr2
            curr2 = curr2.next
        tail = tail.next 
         
    # recursive case   
    return zipper_lists(head_1, head_2, tail, isFirst, count+1, curr1, curr2)

if __name__ == "__main__":
    a = Node("a")
    b = Node("b")
    c = Node("c")
    a.next = b
    b.next = c
    # a -> b -> c

    x = Node("x")
    y = Node("y")
    z = Node("z")
    x.next = y
    y.next = z
    # x -> y -> z

    curr = zipper_lists(a, x)
    # a -> x -> b -> y -> c -> z
    
    while curr.next is not None:
        print(curr.val, end=" -> ")
        curr = curr.next
    print(curr.val, end=" ")
    print("") 
    
    
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

    x = Node("x")
    y = Node("y")
    z = Node("z")
    x.next = y
    y.next = z
    # x -> y -> z

    curr = zipper_lists(a, x)
    # a -> x -> b -> y -> c -> z -> d -> e -> f
    
    while curr.next is not None:
        print(curr.val, end=" -> ")
        curr = curr.next
    print(curr.val, end=" ")
    print("") 
    
    s = Node("s")
    t = Node("t")
    s.next = t
    # s -> t

    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    one.next = two
    two.next = three
    three.next = four
    # 1 -> 2 -> 3 -> 4

    curr = zipper_lists(s, one)
    # s -> 1 -> t -> 2 -> 3 -> 4
    
    while curr.next is not None:
        print(curr.val, end=" -> ")
        curr = curr.next
    print(curr.val, end=" ")
    print("") 
    
    w = Node("w")
    # w

    one = Node(1)
    two = Node(2)
    three = Node(3)
    one.next = two
    two.next = three
    # 1 -> 2 -> 3 

    curr = zipper_lists(w, one)
    # w -> 1 -> 2 -> 3

    while curr.next is not None:
        print(curr.val, end=" -> ")
        curr = curr.next
    print(curr.val, end=" ")
    print("") 
    
    one = Node(1)
    two = Node(2)
    three = Node(3)
    one.next = two
    two.next = three
    # 1 -> 2 -> 3 

    w = Node("w")
    # w

    curr = zipper_lists(one, w)
    # 1 -> w -> 2 -> 3
    
    while curr.next is not None:
        print(curr.val, end=" -> ")
        curr = curr.next
    print(curr.val, end=" ")
    print("") 