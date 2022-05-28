import settings as s
import math


def nbPixels():
    return

# average of an image
def avg(image):
    avg = 0
    for h in range(s.height):
        for w in range(s.width):
            avg += image[h][w]
    return avg / s.width * s.height

# ecartype
def ecartype(image):
    averg = avg(image)
    dev = 0
    for h in range(s.height):
        for w in range(s.width):
            dev += (image[h][w] - averg) ** 2
    return math.sqrt(dev / s.width * s.height)


def histogram(image):
    hist = [0] * (s.graylevel + 1)
    for h in range(s.height):
        for w in range(s.width):
            hist[image[h][w]] += 1
    return hist


def cumulated_histogram(image):
    hist = histogram(image)
    cum_hist = [0] * (s.graylevel + 1)
    cum_hist[0] = hist[0]
    for g in range(1, s.graylevel + 1):
        cum_hist[g] = hist[g] + cum_hist[g - 1]
    return cum_hist