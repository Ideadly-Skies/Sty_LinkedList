class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def is_univalue_list(head, curr_val=None):
    if head is None:
        return True
    if head.val != curr_val:
        if curr_val is not None:
            return False
    return is_univalue_list(head.next, head.val)