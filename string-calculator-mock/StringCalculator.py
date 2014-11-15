class StringCalculator(object):
  def Add(self, operands):
    delimiter = ','
    first_line = operands.split('\n')[0]
    if first_line.startswith('//'):
      delimiter = first_line.split('//')[1]
      operands = '\n'.join(operands.split('\n')[1:])
    return sum([int('0' + x) for x in operands.replace(delimiter, ',').replace('\n', ',').split(',')])
