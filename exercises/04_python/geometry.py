import math

class Point:
   def __init__(self, x, y):
        self.x = x
        self.y = y

   def distance_from( self, newPoint):
     return (math.sqrt((newPoint.x - self.x)**2 + (newPoint.y - self.y)**2))


class Circle:
   def __init__(self, center, radius):
        self.center = center
        self.radius=radius

   def is_inside( self, newPoint):
       if ( ((self.radius)**2) - ((newPoint.x - self.center.x)**2 + (newPoint.y - self.center.y)**2) <= 0 ):
           return (False)
       else:
           return (True)