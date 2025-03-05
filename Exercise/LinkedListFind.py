class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def linked_list_find(head, target):
  if head is None:
    # result is not found
    return False
  elif head.val == target:
    # head matches target 
    return True
  else:
    # iterate forward
    return linked_list_find(head.next, target)
  
if __name__ == "__main__":
  a = Node("a")
  b = Node("b")
  c = Node("c")
  d = Node("d")

  a.next = b
  b.next = c
  c.next = d

  # a -> b -> c -> d

  print(linked_list_find(a, "c")) # True

  a = Node("a")
  b = Node("b")
  c = Node("c")
  d = Node("d")

  a.next = b
  b.next = c
  c.next = d

  # a -> b -> c -> d

  print(linked_list_find(a, "d")) # True

  a = Node("a")
  b = Node("b")
  c = Node("c")
  d = Node("d")

  a.next = b
  b.next = c
  c.next = d

  # a -> b -> c -> d

  print(linked_list_find(a, "q")) # False