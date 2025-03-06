class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def merge_lists(head_1, head_2):
    # init tail pointer for merged list
    current_1 = current_2 = tail = None 

    # set tail to head_1
    if head_1.val < head_2.val:
        tail = head_1
        current_1 = head_1.next
        current_2 = head_2

    if head_2.val < head_1.val:
        tail = head_2
        current_1 = head_1
        current_2 = head_2.next

    # keep iterating until the end of the array
    while (current_1 is not None and current_2 is not None):
        # print(current_1.val)
        # print(current_2.val) 
        
        if (current_1.val < current_2.val):
           tail.next = current_1
           current_1 = current_1.next
        else:
           tail.next = current_2
           current_2 = current_2.next

        # set tail to be tail.next
        tail = tail.next

    # if there are leftovers
    if (current_1 is not None):
       tail.next = current_1
    if (current_2 is not None):
       tail.next = current_2

    # return the head
    if head_1.val < head_2.val:
       return head_1
    else: 
       return head_2

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

    q = Node(1)
    r = Node(8)
    s = Node(9)
    t = Node(10)
    q.next = r
    r.next = s
    s.next = t
    # 1 -> 8 -> 9 -> 10

    node = merge_lists(a, q)
    # 1 -> 5 -> 7 -> 8 -> 9 -> 10 -> 10 -> 12 -> 20 -> 28  

    # print node
    while (node is not None):
       print(node.val)
       node = node.next