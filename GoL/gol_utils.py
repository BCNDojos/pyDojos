import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from time import sleep


def create_world(alive=None,size=3):
    world = np.zeros((size, size), dtype=int)
    if alive:
        for position in alive:
            world[position[0], position[1]] = 1
    return world


def draw_world(world):
    plt.imshow(world, cmap=plt.cm.Greys, interpolation='nearest')


def print_world(world):
    lines = []
    for l in world:
        lines.append("".join(("O" if i else ".") for i in l))
    print "\n".join(lines)


# crear funcio evolve
def evolve(world):
    nm = get_neighbour_matrix(world)-world
    rls = np.vectorize(rules)
    return rls(nm,world)


def get_neighbours(world, pos):
    firstx = max(pos[0]-1, 0)
    lastx = min(pos[0]+1, world.shape[0]-1)
    firsty = max(pos[1]-1, 0)
    lasty = min(pos[1]+1, world.shape[1]-1)
    return world[firstx:lastx+1, firsty:lasty+1]


def get_num_neighbours(world, pos):
    return get_neighbours(world, pos).sum()


def get_neighbour_matrix(world):
    indexs = np.indices(world.shape)
    x = indexs[0]
    y = indexs[1]
    gn = np.vectorize(lambda xx,yy: get_num_neighbours(world,(xx,yy)))
    return gn(x,y)


def rules(num_neighbours, status):
    #If it's alive, with less than 2 neighbors alive, it dies
    if status and num_neighbours < 2:
        return 0
    #If it's alive, with 2 or 3 neighbors alive, it survives
    if status and num_neighbours <=3:
        return 1
    #If it's dead, with exactly 3 other neighbors alive, it born
    if not status and num_neighbours ==3:
        return 1
    #If it's alive, with more than 3 neighbors alive, it dies
    if status and num_neighbours > 3:
        return 0

    return status

def create_random_world(size = None):
    if size is None:
        size = np.random.randint(3,11)
        size = (size,size)
    return np.random.randint(0,2,size)


def update(i):
    global world_
    plt.clf()
    world_ = evolve(world_)
    draw_world(world_)
    fig.canvas.draw()



fig = None
def play(world=None):
    global fig, world_
    if not fig:
        fig = plt.figure()
    try:
        if world is None:
            world = create_random_world()
        world_ = world
        a = anim.FuncAnimation(fig, update, frames=300, repeat=False)
        fig.show()
    except KeyboardInterrupt:
        pass

def play_console(world=None):
    try:
        if world is None:
            world = create_random_world()
        while True:
            world = evolve(world)
            print_world(world)
            print
    except KeyboardInterrupt:
        pass