import gol
import gol_utils
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.animation as anim

# beacon
def get_beacon():
	w = gol_utils.create_world(
		alive=(
			[
				(1,1),(1,2),(2,1),(2,2),
				(3,3),(3,4),(4,3),(4,4)
			]),
		MAX=6
	)    

# Para crear una matriz random
def ger_random():
	return np.random.randint(0,2,(50,50))

def slider(posx,posy,flip=0,invertx=0,inverty=0,MAX=50):
	res = [(2, 0), (3, 0), (0, 1), (1, 1), (3, 1), (4, 1), (0, 2), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3)]

	masx = max( x for x,y in res)
	masy = max( y for x,y in res)	

	if flip:
		res = [(y,-x+masx) for x,y in res]
	
	def invx(v):
		if invertx:
			return masx -v
		else:
			return v
	def invy(v):
		if inverty:
			return masy -v
		else:
			return v

	res = [ (
				invx(x)+posx,
				invy(y)+posy
			) for x,y in res]


	return [ (x,y) for x,y in res if x in range(0,MAX) and y in range(0,MAX) ]

def multi_slider(num):

	w = []
	for a in range(num):
		w += slider( 
				random.randint(0,50),
				random.randint(0,50), 
				random.randint(0,1),
				random.randint(0,1),
				random.randint(0,1),
			)
	return gol_utils.create_world(w,50)


def simple_slider():
	return gol_utils.create_world(
		alive=(
			[
				            (5,3),(6,3),
				(3,4),(4,4),      (6,4),(7,4),
				(3,5),(4,5),(5,5),(6,5),
				      (4,6),(5,6),
			]),
		MAX=30
	) 

w = multi_slider(20)





fig = plt.figure()

def update(i):
	global w
	plt.clf()
	gol_utils.draw_world(w)
	fig.canvas.draw()
	w = gol.evolve(w)
	

a = anim.FuncAnimation(fig, update, frames=3000, repeat=False)
plt.show()
