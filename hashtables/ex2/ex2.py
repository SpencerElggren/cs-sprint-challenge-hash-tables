#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    destinations = [None] * length

    destination_lookup = dict()
    for ticket in tickets:
        destination_lookup[ticket.source] = ticket.destination

    next_destination = destination_lookup["NONE"]

    for current_leg in range(0, length):
        destinations[current_leg] = next_destination
        next_destination = destination_lookup[next_destination]

    return destinations
