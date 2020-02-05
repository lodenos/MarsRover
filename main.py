import sys
from rover import Rover

if len(sys.argv) < 2:
  print "Argument Error"
  exit(-1)
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
    print(rover)
    del rover
