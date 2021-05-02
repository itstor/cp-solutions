import math


def get_participants(handshakes):
    return math.ceil((1+math.sqrt(8*handshakes+1))/2)
