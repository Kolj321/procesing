def setup():
    size(600,400)
    background(random(0,255),0,0)
    frameRate(1000000000)
def draw():
    strokeWeight(random(1,5))
    stroke(random(0,255),0,random(0,255))
    point(random(600),random(400))
    fill(random(0,255),0,random(0,255))
    ellipse(300,200,random(50),random(50))
