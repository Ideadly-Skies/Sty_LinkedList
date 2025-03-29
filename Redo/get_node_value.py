"""
================================

      RECURSIVE SOLUTION

================================
"""
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def get_node_value(head, index, count=0):
    if head is None:
        return None
    if count == index:
        return head.val
    return get_node_value(head.next, index, count+1)

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