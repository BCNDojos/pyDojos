import unittest
import gol
import gol_utils as g

class TestGol(unittest.TestCase):
	def setUp(self):
		self.world = g.create_world(alive=([(0,1),(1,1),(2,1)]))

	def test_vecinas_esquina_izquierda(self):
		posiciones = gol.casillas_vecinas((0,0),3)
		self.assertEqual(set([(0, 1), (1, 0), (1, 1)]),set(posiciones))

	def test_vecinas_esquina_derecha(self):
		posiciones = gol.casillas_vecinas((2,0),3)
		self.assertEqual(set([(1, 0), (1, 1), (2, 1)]),set(posiciones))

	def test_superior(self):
		cuantos = gol.numero_vecinos(self.world,(0,1))
		self.assertEqual(cuantos,1)

	def test_esquina(self):
		cuantos = gol.numero_vecinos(self.world,(0,0))
		self.assertEqual(cuantos,2)		

	def test_medio(self):
		cuantos = gol.numero_vecinos(self.world,(1,0))
		self.assertEqual(cuantos,3)		


class TestEndToEnd(unittest.TestCase):

	def test_flipflop(self):

		w1 = g.create_world(alive=([(0,1),(1,1),(2,1)]))
		w2 = g.create_world(alive=([(1,0),(1,1),(1,2)]))

		self.assertTrue((gol.evolve(w1) != w2).sum()==0)
		self.assertTrue((gol.evolve(w2) != w1).sum() ==0)


if __name__ == "__main__":
	unittest.main()