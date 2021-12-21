from Parser import Parser
from Rover import Rover
from Direction import Direction
from Position import Position
from Instructions import *

import signal

TIMEOUT = 10 # number of seconds your want for timeout


class Mission:
    map_coordinates = (5, 5)
    mission_is_active = True

    def interrupted(self, signum, frame):
        print('Input times out...')
        exit
    
    def verify_initial_coordinates(self, initial_coordinates):
        if (initial_coordinates[0] > self.map_coordinates[0] or
            initial_coordinates[1] > self.map_coordinates[1]):
            print("wrong coordinates default set")
            return False
        return True
    

    def executeMove(self, instructions):
        for instruction in instructions:
            if (instruction == MOVE):
                self.rover.move_forward()
            elif (instruction == RIGHT):
                self.rover.turn_right()
            elif (instruction == LEFT):
                self.rover.turn_left()
        print("pos x : " + str(self.rover.position.pos_x) + " pos y : " + str(self.rover.position.pos_y))

    def initialize_rover(self, parser):
        self.map_coordinates = parser.getMap(input())
        if not (self.map_coordinates): self.map_coordinates = (5, 5)
        print(self.map_coordinates)

        initial_coordinates = parser.getInitialPosition(input())
        if not (self.verify_initial_coordinates(initial_coordinates)): initial_coordinates = (0, 0, "N")

        print(initial_coordinates)

        return Rover(Position(initial_coordinates[0], initial_coordinates[1]), Direction(initial_coordinates[2]))

    def startMission(self):
        signal.signal(signal.SIGALRM, self.interrupted)
        print("Please enter the map coordinates like: 5 5")

        parser = Parser()
        self.rover = self.initialize_rover(parser)

        while self.mission_is_active:
            signal.alarm(TIMEOUT)
            instructions = parser.getMove(input())
            self.executeMove(instructions)
            signal.alarm(0)

