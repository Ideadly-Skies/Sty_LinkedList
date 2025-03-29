class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def insert_node(head, value, index, prev=None, curr=None, isFirst=True, count=0):
    # init pointers
    if isFirst:
        curr = head
        isFirst = False
    
    # insert at index 
    if count == index:
        # init new_node 
        new_node = Node(value) 
        
        # begin insert    
        if prev is None:
            # insert at beginning
            new_node.next = head 
            return new_node
        elif curr is None:
            # insert at the end  
            prev.next = new_node 
        else: 
            # insert at middle 
            prev.next = new_node
            new_node.next = curr
        # return head of linkedlist 
        return head 
    
    # recursive case 
    return insert_node(head, value, index, curr, curr.next, isFirst, count+1)