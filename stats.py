import settings as s
import math
import TP1

def nbPixels():
    return s.width * s.height

def entropy(image):
    hist = TP1.histogram(image)
    ent = 0
    for g in range(s.graylevel + 1):
        p = hist[g] / nbPixels()
        if (p != 0):
            ent += p * math.log2(1 / p)
    return ent

def dynamic(image):
    hist = TP1.histogram(image)
    dmin, dmax = 0, s.graylevel
    for g in range(s.graylevel + 1):
        if (hist[g] == 0):
            continue
        else:
            dmin = g
            break
    for g in reversed(range(s.graylevel + 1)):
        if (hist[g] == 0):
            continue
        else:
            dmax = g
            break
    return dmin, dmax


def SNR(image):
    avg = TP1.avg(s.image_orig)
    S = 0
    B = 0
    for h in range(s.height):
        for w in range(s.width):
            S += (s.image_orig[h][w] - avg) ** 2
            B += (image[h][w] - s.image_orig[h][w]) ** 2
    if (B == 0):
        return 0.0
    if(S<0) :
        return 0.0
    if(B<0):
        return 0.0
    return math.sqrt(S / B)
