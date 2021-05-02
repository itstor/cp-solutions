import math


def rgb(r, g, b):
    hexcode = ["0", "1", "2", "3", "4", "5", "6",
               "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    rgbin = [r, g, b]
    colorcode = []
    for i in rgbin:
        if(i <= 255 and i >= 0):
            color1 = hexcode[math.floor(i/16)]
            color2 = hexcode[int(((i/16)-math.floor(i/16))*16)]
        elif (i > 255):
            color1, color2 = "F", "F"
        else:
            color1, color2 = 0, 0
        colorcode.append(color1)
        colorcode.append(color2)

    return "".join(str(i) for i in colorcode)
