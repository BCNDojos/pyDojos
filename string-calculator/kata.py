class StringCalculator(object):
    def Add(self, operands):
        if len(operands) == 0:
            return len(operands)
        n = operands.split(',')
        if len(n) == 1:
            return int(n[0])
        return int(n[0]) + int(n[1])
