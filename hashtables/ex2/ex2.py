#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    c = {}
    for ticket in tickets:
        c[ticket.source] = ticket.destination

    itenerary = []

    for _ in range(length):
        itenerary.append(c[itenerary[-1]] if len(itenerary) > 0 else c['NONE'])

    return itenerary
