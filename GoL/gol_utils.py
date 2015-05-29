import numpy as np
import matplotlib.pyplot as plt

def create_world(alive = None):
    world = np.zeros((3,3), dtype=int)
    if alive:
        for position in alive:
            world[position[0], position[1]] = 1
    return world

def draw_world(world):
    plt.imshow(world, cmap=plt.cm.Greys, interpolation='nearest')
