class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def merge_lists(head_1, head_2, curr1=None, curr2=None, tail=None, isFirst=True):
    # if curr1:
    #     print("curr1: %s" %(curr1.val))
    # if curr2:
    #     print("curr2: %s" %(curr2.val))
    if tail:
        print("tail: %s" %(tail.val))
    
    # base case 1 
    if curr1 is None and not isFirst:
        tail.next = curr2
        
        if head_1.val < head_2.val:
            return head_1
        else: 
            return head_2
    # base case 2
    if curr2 is None and not isFirst:
        tail.next = curr1
        
        if head_1.val < head_2.val:
            return head_1
        else:
            return head_2 
    
    # init pointers 
    if isFirst:
        if head_1.val < head_2.val:
            tail = head_1
            curr1 = head_1.next
            curr2 = head_2
        else:
            tail = head_2
            curr1 = head_1 
            curr2 = head_2.next
        isFirst = False
    else:
        if curr1.val < curr2.val:
            tail.next = curr1
            curr1 = curr1.next
        else:
            tail.next = curr2
            curr2 = curr2.next
        tail = tail.next
    
    # recursive case
    return merge_lists(head_1, head_2, curr1, curr2, tail, isFirst) 

if __name__ == "__main__":
    a = Node(5)
    b = Node(7)
    c = Node(10)
    d = Node(12)
    e = Node(20)
    f = Node(28)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    # 5 -> 7 -> 10 -> 12 -> 20 -> 28

    q = Node(6)
    r = Node(8)
    s = Node(9)
    t = Node(25)
    q.next = r
    r.next = s
    s.next = t
    # 6 -> 8 -> 9 -> 25

    curr = merge_lists(a, q)
    # 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 12 -> 20 -> 25 -> 28 
    
    while curr.next is not None:
        print(curr.val, end=" -> ")
        curr = curr.next
    print(curr.val, end=" ")
    print("") 
    
    a = Node(5)
    b = Node(7)
    c = Node(10)
    d = Node(12)
    e = Node(20)
    f = Node(28)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    # 5 -> 7 -> 10 -> 12 -> 20 -> 28

    q = Node(1)
    r = Node(8)
    s = Node(9)
    t = Node(10)
    q.next = r
    r.next = s
    s.next = t
    # 1 -> 8 -> 9 -> 10

    curr = merge_lists(a, q)
    # 1 -> 5 -> 7 -> 8 -> 9 -> 10 -> 10 -> 12 -> 20 -> 28 

    while curr.next is not None:
        print(curr.val, end=" -> ")
        curr = curr.next
    print(curr.val, end=" ")
    print("") 
    
    
    h = Node(30)
    # 30

    p = Node(15)
    q = Node(67)
    p.next = q
    # 15 -> 67

    curr = merge_lists(h, p)
    # 15 -> 30 -> 67
    
    while curr.next is not None:
        print(curr.val, end=" -> ")
        curr = curr.next
    print(curr.val, end=" ")
    print("") 