import math

def getVolume(r):
    return ((4 * math.pi * pow(r, 3)) / 3)


def getSurfaceArea(r):
    return 4 * math.pi * pow(r, 2)


def truncate(n, d=0):
    m = 10 ** d
    return int(n * m) / m


radius = int(input("Please enter radius: "))
volume = truncate(getVolume(radius), 2)
area = truncate(getSurfaceArea(radius), 2)

print("Volume: " + repr(volume))
print("Surface: " + repr(area))