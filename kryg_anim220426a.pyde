x = 0
def setup():
  size(500,500)
def draw():
  global x
  background(100)
  ellipse(x,x, 20,20)
  x = x + 1
