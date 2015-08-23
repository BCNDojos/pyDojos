#!/usr/bin/env python

import unittest

MONEDERO_EUR = {'5c': 2, '10c': 2, '20c': 2, '50c': 2, '1e': 2, '2e': 1}
MONEDERO_USD = {'5c': 4, '10c': 3, '25c': 2, '50c': 5, '1d': 2}

def coins(cantidad, currency):
    assert type(cantidad) is float
    monedero = MONEDERO_EUR if currency == 'EUR' else MONEDERO_USD
    cantidad = int(cantidad * 100)
    monedas = {
            'EUR': [200, 100, 50, 20, 10, 5],
            'USD': [100, 50, 25, 10, 5]}
    denominaciones = {
            'EUR': ['2e', '1e', '50c', '20c', '10c', '5c'],
            'USD': ['1d', '50c', '25c', '10c', '5c']}
    resultado = {}
    for m, d in zip(monedas[currency], denominaciones[currency]):
        cuenta, cantidad = divmod(cantidad, m)
        if cuenta != 0:
            if cuenta <= monedero[d]:
                resultado[d] = cuenta
            else:
                resultado[d] = monedero[d]
                cantidad += (cuenta - monedero[d]) * m
    return resultado

class TestCoins(unittest.TestCase):

    currency = 'EUR'
    resultados_mvp = [
            {'5c': 1, '20c': 1},
            {'5c': 1, '10c': 1, '20c': 1, '2e': 1},
            {'1e': 1, '2e': 1},
            {'10c': 1, '20c': 2, '50c': 2, '1e': 2, '2e': 1}]
    cantidades_mvp = [
            0.25,
            2.35,
            3.00,
            5.50]

    def test_00_5_centimos(self):
        resultado = coins(0.05, self.currency)
        self.assertEqual({'5c': 1}, resultado, "5 centimos en una moneda")

    def test_01_50_centimos(self):
        resultado = coins(0.5, self.currency)
        self.assertEqual({'50c': 1}, resultado, "50 centimos en una moneda")

    def test_02_mvp(self):
        for i, cantidad in enumerate(self.cantidades_mvp):
          resultado = coins(cantidad, self.currency)
          self.assertEqual(self.resultados_mvp[i], resultado, "{} centimos".format(cantidad))

class TestCoinsUSD(TestCoins):

    currency = 'USD'
    resultados_mvp = [
            {'25c': 1},
            {'10c': 1, '25c': 1, '1d': 2},
            {'50c': 2, '1d': 2},
            {'5c': 4, '10c': 3, '25c': 2, '50c': 5, '1d': 2}]
    cantidades_mvp = [
            0.25,
            2.35,
            3.00,
            5.50]

if __name__ == '__main__':
    unittest.main()
