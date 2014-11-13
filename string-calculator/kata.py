class StringCalculator(object):
  def Add(self, operands):
    delimiter = ''
    return sum([int("0" + x) for x in operands.replace(delimiter, ",").replace("\n", ",").split(",")])
