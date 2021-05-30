from swampy.TurtleWorld import *


def square(t, length):
    for i in range(4):
        fd(t, length)
        lt(t)


world = TurtleWorld()
bob = Turtle()
print(bob)
square(bob, 50)
square(bob, 100)
square(bob, 150)

wait_for_user()
