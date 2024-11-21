EAST = 0
NORTH = 1
WEST = 2
SOUTH = 3


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self._coordinates = [x_pos, y_pos]

    @property
    def coordinates(self):
        return tuple(self._coordinates)

    def move(self, instructions: str):
        if not instructions:
            return
        instruction, instructions = instructions[0], instructions[1:]
        match instruction:
            case 'R' | 'L':
                self.direction += 1 if instruction == 'L' else -1
                self.direction %= 4
            case 'A':
                if self.direction == EAST:
                    self._coordinates[0] += 1
                elif self.direction == WEST:
                    self._coordinates[0] -= 1
                elif self.direction == NORTH:
                    self._coordinates[1] += 1
                else:
                    self._coordinates[1] -= 1
        self.move(instructions)
