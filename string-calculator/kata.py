class StringCalculator(object):
  def Add(self, operands):
    n = 0
    for x in operands.split(','):
      if len(x) > 0:
        n += int(x)
    return n
