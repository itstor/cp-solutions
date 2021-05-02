def time_convert(num):
    return "00:00" if num < 1 else str(num//60).zfill(2) + ":" + str(num % 60).zfill(2)
