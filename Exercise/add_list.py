class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# iterative version
def add_lists(head_1, head_2, carry=0):
    # both of my input list are going to be of the same length
    if head_1 is None and head_2 is None and carry == 0:
       return None

    # compute both value of head
    val_1 = 0 if head_1 is None else head_1.val
    val_2 = 0 if head_2 is None else head_2.val

    # compute their sum 
    sum = val_1 + val_2 + carry
    next_carry = 1 if sum > 9 else 0 # carry logic 

    # compute digit
    digit = sum % 10
    result = Node(digit)

    # only recurse if head_1 and head_2 next pointer is not None 
    next_1 = None if head_1 is None else head_1.next
    next_2 = None if head_2 is None else head_2.next

    # assign the next node to the sum of the next two nodes
    result.next = add_lists(next_1, next_2, next_carry)
    
    return result