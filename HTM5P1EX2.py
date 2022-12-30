
class Point:
	
	def __init__(self, x, y):
		self.__x = x
		self.__y = y

	@property
	def x(self):
		return self.__x

	@property
	def y(self):
		return self.__y

	def dist(self, p):
		from math import sqrt
		return((self.x - p.x) ** 2 + (self.y - p.y) ** 2)

p = Point(0, 0)
q = Point(1, 1)
print(p.dist(q))