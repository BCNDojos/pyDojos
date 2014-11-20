import sys
from StringCalculator import StringCalculator


def main(string_calculator, argv):
    line = argv[1]
    while line:
        print(string_calculator.Add(line))
        line = raw_input('Otra entrada, por favor ').strip()
        print

if __name__ == '__main__':
    main(StringCalculator(), sys.argv)
