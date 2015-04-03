import unittest
from unittest.mock import patch
from pos import POS
import store

class TestPOS(unittest.TestCase):
    def setUp(self):
        prices = None
        test_name = self.id().split('.')[-1]
        if test_name == 'test_priced_list':
            prices = {
                '293002910392': 5.0,
                '098364849832': 0.95,
            }
        self.pos = POS(prices)
        
    @patch.object(store.Store, 'lock', return_value = None)
    def test_simple_list(self, mock_store):
        self.pos.scan('293002910392', 2)
        mock_store.assert_called_with('293002910392', 2)
        self.assertEqual(len(self.pos.list()), 1)
        self.pos.scan('098364849832', 10)
        mock_store.assert_called_with('098364849832', 10)
        result = self.pos.list()
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0][0], '293002910392')
        self.assertEqual(result[0][1], 2)
        self.assertEqual(result[1][0], '098364849832')
        self.assertEqual(result[1][1], 10)

    @patch.object(store.Store, 'lock', return_value = None)
    def test_priced_list(self, mock_store):
        self.pos.scan('293002910392', 2)
        mock_store.assert_called_with('293002910392', 2)
        self.assertEqual(len(self.pos.list()), 1)
        self.pos.scan('098364849832', 10)
        mock_store.assert_called_with('098364849832', 10)
        result = self.pos.list()
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0][0], '293002910392')
        self.assertEqual(result[0][1], 2)
        self.assertEqual(result[0][2], 5.0)
        self.assertEqual(result[0][3], 10.0)
        self.assertEqual(result[1][0], '098364849832')
        self.assertEqual(result[1][1], 10)
        self.assertEqual(result[1][2], 0.95)
        self.assertEqual(result[1][3], 9.5)

if __name__ == '__main__':
    unittest.main()