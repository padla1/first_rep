import time


def make_readable(seconds):
    return  time.strftime ("%H:%M:%S", time.gmtime(seconds))


print(make_readable(86400))


