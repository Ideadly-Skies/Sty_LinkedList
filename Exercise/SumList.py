class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def sum_list(head):
  if head is None:
    return 0
  return head.val + sum_list(head.next)

if __name__ == "__main__":
    a = Node(2)
    b = Node(8)
    c = Node(3)
    d = Node(-1)
    e = Node(7)

    a.next = b
    b.next = c
    c.next = d
    d.next = e

    # 2 -> 8 -> 3 -> -1 -> 7

    print(sum_list(a)) # 19