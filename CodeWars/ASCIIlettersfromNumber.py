def convert(number):
    return "".join(chr(int(a)) for a in [number[i:i+2] for i in range(0, len(number), 2)])
