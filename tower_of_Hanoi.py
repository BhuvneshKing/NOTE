'''
The game consists of three sticks, on which several perforated discs are placed, all of different sizes.
At the beginning, all the discs are on the left stick, arranged in order of size, with the largest disc on the bottom and the smallest on the top.
The object of the game is to move the entire stack of discs to the right stick.
However, only a smaller disc may be placed on a larger one, a larger one on a smaller one is not allowed.
'''
def move(disc, source, destination, aux):
    if disc > 0:
        move(disc - 1, source, aux, destination)
        print("Disc " + str(disc) + ": move from " + str(source) + " to " + str(destination))
        move(disc - 1, aux, destination, source)


move(4, "left", "middle", "rigth")