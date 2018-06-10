from collections import namedtuple
from functools import reduce
from itertools import cycle
from operator import add


Robot = namedtuple('Robot', ('x', 'y', 'direction'))
direction = cycle(('NORTH', 'EAST', 'SOUTH', 'WEST'))


def turn_right(robot):
    if next(direction) != robot.direction:
        return turn_right(robot)
    return Robot(robot.x, robot.y, next(direction))


def turn_left(robot):
    return turn_right(turn_right(turn_right(robot)))


def advance(robot):
    advance_map = {
        'NORTH': (0, 1),
        'EAST': (1, 0),
        'SOUTH': (0, -1),
        'WEST': (-1, 0)
    }
    new_coordinates = map(add, (robot.x, robot.y), advance_map[robot.direction])
    return Robot(*new_coordinates, robot.direction)


def move(robot, command):
    movement_map = {
        'A': advance,
        'L': turn_left,
        'R': turn_right
    }
    return movement_map[command](robot)


def execute_commands(robot, commands):
    if not commands:
        return robot
    head_command, *tail_commands = commands
    return execute_commands(move(robot, head_command), tail_commands)


def print_position(robot):
    print(robot.x, robot.y, robot.direction)


if __name__ == '__main__':
    robot_position = input('Robot position:\n').split()
    robot_position = *map(int, robot_position[:2]), robot_position[2]
    commands = input('Commands:\n')
    print_position(execute_commands(Robot(*robot_position), commands))
