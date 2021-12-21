from Instructions import * 

class Rover:

    def __init__(self, position, direction):
        self.position = position
        self.direction = direction
    
    def turn_right(self):
        if (self.direction.direction is not directions_list[len(directions_list) - 1]):
            self.direction.direction = directions_list[directions_list.index(self.direction.direction) + 1]
        else:
            self.direction.direction = directions_list[0]

    def turn_left(self):
        if (self.direction.direction is directions_list[0]):
            self.direction.direction = directions_list[len(directions_list) - 1]
        else:
            self.direction.direction = directions_list[directions_list.index(self.direction.direction) - 1]

    def move_forward(self):
        if (self.direction.direction == NORTH):
            self.position.pos_y += 1
        elif (self.direction.direction == SOUTH): 
            self.position.pos_y -= 1
        elif (self.direction.direction == EAST):
            self.position.pos_x += 1
        else:
            self.position.pos_x -= 1
