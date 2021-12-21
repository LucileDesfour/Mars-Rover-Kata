from Instructions import instruction_list, directions_list
from Exceptions import InputError

class Parser():

    def getMap(self, line):
        coordinates = line.split()
        return self.getCoordinates(coordinates)
    
    def getInitialPosition(self, line):
        initial_position = line.split()
        coordinates = self.getCoordinates(initial_position)
        if not coordinates:
            print("Invalid coordinates " + str(coordinates) + " return default")
            return(0, 0, "N")
        if (len(initial_position) == 3 and initial_position[2] in directions_list):
            return (coordinates[0], coordinates[1], initial_position[2])
        print("Invalid direction " + str(initial_position) + " return default")
        return(0, 0, "N")

    def getCoordinates(self, coordinates):
        try:
            int(coordinates[0])
            int(coordinates[1])
        except:
            return
        return (int(coordinates[0]), int(coordinates[1]))

    
    def getMove(self, line):
        line_list = list(line)
        result = map(lambda char: char in instruction_list, line_list)
        if not (all(item in instruction_list for item in line_list)):
            raise InputError(line, "One of the instruction is not in the list " + str(instruction_list))
        return line_list