class StringCalculator(object):
  def Add(self, operands):
    return sum([int("0" + x) for x in operands.replace("\n", ",").split(",")])
