#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(self, tickets):
    """
    YOUR CODE HERE
    """
    # Your code here
    d = {}
    # for loop through the tickets
    for i in tickets:
        if self.source is None:
            i += d[i]
        if self.source is self.destination:
            i += d[i]
        if self.desitnation is self.source:
            i += d[i]
    
    for j in d:
        route.append(j)

    # create route
    route = []
    #orgnize the tickets


    return route
