import sys #For ANSI escape sequences.
import Getch as g #For getting input without waiting for enter hits

class Pos():
  def __init__(self,r,c):
    self.r=r
    self.c=c

class World():
  validChars = []

  #There is a variable "map"
  def __init__(self):
    self.map = [[self.startWall(j,i) for i in range(20)] for j in range(10)]
    self.pos = Pos(5,5)
    self.getch = g._Getch()
    self.hp = 9
    
  def startWall(self,r,c):
    if r==0 or c==0 or r==9 or c==19:
      return 'X'
    return '.'

  def go(self,rmod,cmod):
    r = self.pos.r
    c = self.pos.c
    if self.map[r+rmod][c+cmod] != 'X':
      self.pos.r += rmod
      self.pos.c += cmod
    else:
      self.hp -= 1

  def play(self):
    self.display()
    inchar = self.getch()
    if ord(inchar) != 27:
      return False
    self.getch() #Should always be ord 91
    inchar = self.getch() #65-68 are UP, DOWN, RIGHT, LEFT
    if ord(inchar) == 65:
      self.go(-1,0)
    elif ord(inchar) == 66:
      self.go(1,0)
    elif ord(inchar) == 67:
      self.go(0,1)
    elif ord(inchar) == 68:
      self.go(0,-1)
    else:
      return False
    self.display()
    if self.hp == 0:
      self.displayGameOver()
      return False
    return True

  def display(self):
    sys.stdout.write('\x1b[2J') #Clear the screen and reset the curser
#    for i in range(31,38):
#      sys.stdout.write('\x1b[%sm%s\x1b[0m' % (i,'E'))
#    sys.stdout.write('\n')
    for r in range(10):
      for c in range(20):
        if self.pos.r == r and self.pos.c == c:
          sys.stdout.write('\x1b[%sm%s\x1b[0m' % ('33',str(self.hp)))
        else:
          sys.stdout.write(self.map[r][c])
      sys.stdout.write('\n')
      sys.stdout.flush()
      
  def displayGameOver(self):
    sys.stdout.write('\x1b[%sm%s\x1b[0m' % (';'.join(['31','1']),
          '     GAME OVER\n'))
    sys.stdout.flush()

myWorld = World()
while myWorld.play():
  pass
