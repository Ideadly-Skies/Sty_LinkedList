class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def longest_streak(head, val=0, counter=1, first=True, max_streak=0):
    # return 0 longest streak 
    if head is None:
       return 0 
    
    # base case reached
    elif head.next is None:
        # sole node
        if first:
          return counter

        # break the streak
        if head.val != val:
           # update max_streak and counter
           max_streak = max(max_streak, counter)
           counter = 1
        else:
           # increment counter and max_streak
           counter += 1
           max_streak = max(max_streak, counter)

        # return max_streak
        return max_streak
    elif first:
        # skip over first node
        first = False 
    else:
        # break the streak and update max_streak
        if head.val != val:
            max_streak = max(max_streak, counter)
            counter = 1
        else:
           # increment the streak and update max_streak
           counter += 1
           max_streak = max(max_streak, counter)

    return longest_streak(head.next, head.val, counter, first, max_streak) 

if __name__ == "__main__":
    a = Node(3)
    b = Node(3)
    c = Node(3)
    d = Node(3)
    e = Node(9)
    f = Node(9)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    # 3 -> 3 -> 3 -> 3 -> 9 -> 9

    print(longest_streak(a)) # 4