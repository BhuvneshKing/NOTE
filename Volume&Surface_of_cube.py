def getVolume(a):
    volume = a * a * a
    return volume


def getSurface(a):
    surface = 6 * a * a
    return surface


edgeLength = int(input("Please enter the edge length: "))
print("Volume: " + repr(getVolume(edgeLength)))
print("Surface: " + repr(getSurface(edgeLength)))