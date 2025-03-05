class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# def linked_list_values(head):
#     """
#     append linked list values to ls 
#     """
#     # list to store linked list values
#     ls = []

#     # iterative solution
#     current = head
#     while current is not None:
#         ls.append(current.val)
#         current = current.next

#     # return a list containing the value
#     return ls

def linked_list_values(head):
    """
    append linked list values to ls recursively 
    """
    # recursive solution 
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