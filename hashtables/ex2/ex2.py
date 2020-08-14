# from hashtables import (Hashtable, put, delete, resize, get)


#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    # create route
    hashtable = {}
    route = [None] * length

    for i in range(length):
        # 
        if tickets[i].source == "NONE":
            route[0] = tickets[i].destination
        hashtable[tickets[i].source] = tickets[i].destination
    
    for j in range(length):
        if route[j - 1] is not None:
            route[j] = hashtable[route[j - 1]]
    

    return route
