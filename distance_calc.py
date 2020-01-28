from math import sqrt

def distance2d(a, b):
	diffX = abs(a[0] - b[0])
	diffY = abs(a[1] - b[1])
	delta = sqrt((diffX ** 2) + (diffY ** 2))
	return delta
	
def distance3d(a, b):
	a2d = (a[0], a[2])
	b2d = (b[0], b[2])
	diffX = distance2d(a2d, b2d)
	diffY = abs(a[1] - b[1])
	delta = sqrt((diffX ** 2) + (diffY ** 2))
	return delta
	
if __name__ == "__main__":
	print(
		distance3d(
			(1, 2, 3),
			(4, 5, 6)
		)
	)