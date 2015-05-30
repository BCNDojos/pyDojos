import gol_utils as g



world = g.create_world(alive=([(0,1),(1,1),(2,1)]))

def casillas_vecinas( pos, MAX):
	"""Retorna Lista de casillas vecinas validas"""

	xpos, ypos = pos

	posiciones = [ 
		(x,y) 
		for x in range(xpos-1, xpos+2) if x >= 0 and x <MAX
		for y in range(ypos-1, ypos+2) if y >= 0 and y <MAX and not (x==xpos and y==ypos) 
		]
	return posiciones

#print casillas_vecinas((0,0),MAX)


def numero_vecinos( world, pos):
	"""Retorna el numero de vecions vivos de una casilla"""

	xpos, ypos = pos

	valores = [  world[p[0],p[1]] for p in casillas_vecinas(pos,world.shape[0]) ]
	return sum(valores)


def evolve(world):
	"""Recorre el mundo creando una nuevo"""

	dim = world.shape[0]
	nuevo_mundo = g.create_world( [

		(x,y)
		for x in range(0,dim)
		for y in range(0,dim)
		if ( (world[x,y] and numero_vecinos(world,(x,y))==2) 
		      or numero_vecinos(world,(x,y))==3)
		   
	  ],
	  dim

	)
	return nuevo_mundo

#w1 = evolve(world)
#print w1

#print evolve(w1)










