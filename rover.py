class Rover:
  __mapLeft = {
    'N': 'W',
    'W': 'S',
    'S': 'E',
    'E': 'N'
  }
  __mapRight = {
    'N': 'E',
    'E': 'S',
    'S': 'W',
    'W': 'N'
  }
  __mapMove = {
    'N': [0, 1],
    'E': [1, 0],
    'S': [0, -1],
    'W': [-1, 0]
  }

  def __init__(self, x, y, direction):
    self._x = x
    self._y = y
    self._direction = direction

  def __str__(self):
    return '%d %d %c' % (self._x, self._y, self._direction)

  def interpreter(self, instruction):
    [self.__instruction[index](self) for index in instruction]

  def move(self):
    vecor = self.__mapMove[self._direction]
    self._x += vecor[0]
    self._y += vecor[1]

  def turn_left(self):
    self._direction = self.__mapLeft[self._direction]

  def turn_right(self):
    self._direction = self.__mapRight[self._direction]

  __instruction = {
    'M': move,
    'R': turn_right,
    'L': turn_left
  }
