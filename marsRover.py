import sys

class Rover:
  _x = 0
  _y = 0
  _direction = 'N'
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

  def move(self):
    vecor = self.__mapMove[self._direction]
    self._x += vecor[0]
    self._y += vecor[1]

  def print_status(self):
    print self._x, self._y, self._direction

  def turn_left(self):
    self._direction = self.__mapLeft[self._direction]

  def turn_right(self):
    self._direction = self.__mapRight[self._direction]

  __instruction = {
    'M': move,
    'R': turn_right,
    'L': turn_left
  }

  def interpreter(self, instruction):
    [self.__instruction[index](self) for index in instruction]

if __name__ == '__main__':
  if len(sys.argv) < 2:
    print "Argument Error"
    exit(-1)
  listRover = []
  with open(sys.argv[1]) as file:
    data = file.read().split('\n')
    data = [data[2::2], data[1::2]]
    for index in range(len(data[0])):
      instruction = data[0][index]
      position = data[1][index].split(" ")
      if len(position) != 3:
        print "Error Position"
        exit(-1)
      rover = Rover(int(position[0]), int(position[1]), position[2])
      rover.interpreter(instruction)
      rover.print_status()
      del rover
