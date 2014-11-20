#!/usr/bin/env python

import unittest
import mock
import sys
from StringIO import StringIO
from StringCalculator import StringCalculator
import kata


class TestKata(unittest.TestCase):
    def setUp(self):
        self.string_calculator = StringCalculator()
        self.string_calculator.Add = mock.Mock()
        sys.stdout = StringIO()
        sys.stdin = StringIO('\n')

    def tearDown(self):
        sys.stdout = sys.__stdout__
        sys.stdin = sys.__stdin__

    def test_first_input_from_command_line_argument(self):
        kata.main(self.string_calculator, ['_', '1,2,3,4'])
        self.string_calculator.Add.assert_called_once_with('1,2,3,4')

    def test_output_with_once_input(self):
        self.string_calculator.Add.return_value = '10'
        kata.main(self.string_calculator, ['_', '1,2,3,4'])
        self.assertEquals(sys.stdout.getvalue().split('\n'), ['10', 'Otra entrada, por favor ', ''])

    def test_output_with_multiple_inputs(self):
        self.string_calculator.Add.side_effect = ['10', '6']
        sys.stdin = StringIO('1,2,3\n\n')
        kata.main(self.string_calculator, ['_', '1,2,3,4'])
        self.assertEquals(
            sys.stdout.getvalue().split('\n'),
            ['10', 'Otra entrada, por favor ', '6', 'Otra entrada, por favor ', '']
        )


if __name__ == '__main__':
    unittest.main()

