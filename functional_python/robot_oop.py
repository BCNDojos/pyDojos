directions = ['North', 'East', 'South', 'West']


class Robot:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    @property
    def position(self):
        return self.x, self.y, self.direction

    def turn_right(self):
        self.direction = directions[(directions.index(self.direction) + 1) % 4]

    def turn_left(self):
        self.direction = directions[(directions.index(self.direction) + 3) % 4]

    def advance(self):
        direction = self.position[2]
        if direction == 'North':
            self.y += 1
        if direction == 'East':
            self.x += 1
        if direction == 'South':
            self.y -= 1
        if direction == 'West':
            self.x -= 1

    def move(self, letter):
        if letter == 'R':
            self.turn_right()
        if letter == 'L':
            self.turn_left()
        if letter == 'A':
            self.advance()

    def execute_movements(self, s):
        for letter in s:
            self.move(letter)


if __name__=='__main__':
    input1 = input('Robot starting position:\n').split()
    x = int(input1[0])
    y = int(input1[1])
    direction = input1[2]
    robot = Robot(x, y, direction)
    input2 = input('Movements:\n')
    robot.execute_movements(input2)
    print(robot.position)
