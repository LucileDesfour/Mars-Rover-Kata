from Instructions import directions_list

from Exceptions import InputError

class Direction:
    def __init__(self, direction):
        self.verify_direction(direction)
        self.direction = direction

    def verify_direction(self, direction):
        if (direction not in directions_list):
            raise InputError(direction, 'This direction is not available, choose between ' + str(directions).strip('[]'))