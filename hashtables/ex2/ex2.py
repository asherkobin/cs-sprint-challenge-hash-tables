#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    route_table = {}
    route = []

    # load the table

    for ticket in tickets:
      route_table[ticket.source] = ticket.destination

    # prepare
    
    destination = route_table["NONE"]

    # find the next destination until it is NONE
    
    while destination is not "NONE":
      route.append(destination)
      destination = route_table[destination]

    route.append("NONE") # tests want this

    return route
