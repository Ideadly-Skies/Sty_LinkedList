# """
# ================================

#       ITERATIVE SOLUTION

# ================================
# """
# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

# def linked_list_values(head):
#     values = []
    
#     while (head is not None):
#         values.append(head.val)
#         head = head.next
    
#     return values

"""
================================

      RECURSIVE SOLUTION

================================
"""
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def linked_list_values(head):
    if head is None:
        return []
    
    return [head.val] + linked_list_values(head.next)

if __name__ == "__main__":
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.next = b
    b.next = c
    c.next = d

    # a -> b -> c -> d

    print(linked_list_values(a)) # -> [ 'a', 'b', 'c', 'd' ]
    
    x = Node("x")
    y = Node("y")

    x.next = y

    # x -> y

    print(linked_list_values(x)) # -> [ 'x', 'y' ]
    
    q = Node("q")

    # q

    print(linked_list_values(q)) # -> [ 'q' ]