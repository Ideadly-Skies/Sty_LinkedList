class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def remove_node(head, target_val, prev=None, curr=None):
    if (curr is None):
        # set curr to head.next 
        curr = head.next 
        prev = head

        # remove one and only node
        if (prev.val == target_val):
            return curr 
    
    # remove first node and sole node
    elif (prev.val == target_val):
        return curr    
    # remove subsequent and last node 
    elif (curr.val == target_val):
        # remove last node 
        if (curr.next is None and prev is not None):
            prev.next = None
        # remove subsequent nodes 
        else: 
            prev.next = curr.next
            curr = None # clean curr pointer
        return head
    else:
        # increment pointers
        curr = curr.next
        prev = prev.next
    
    # recursive case 
    return remove_node(head, target_val, prev, curr)

if __name__ == "__main__":
    t = Node("t")

    # t

    node = remove_node(t, "t")
    # None

    while (node is not None):
        print(node)
        node = node.next