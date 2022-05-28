import settings as s
import utils


# TP1
# functions to read PGM and PPM  img from img file

def read(filepath):
    #we need to define the img type at first
    type = getType(filepath)
    if (type == None):
        raise Exception
    if (type == "P2\n"):
        imageread, s.width, s.height, s.graylevel = getAscii(filepath)

    else:
        imageread, s.width, s.height, s.graylevel = getBinary(filepath)
    if (imageread == None):
        raise Exception
    else:
        s.isread = True
        s.image_orig = utils.arrayToMatrix(imageread, s.width, s.height)

# determine type functiopn
def getType(filepath):
    try:
        file = open(filepath, 'r')
        type = file.readline()
    except UnicodeDecodeError:
        file = open(filepath, 'rb')
        type = file.readline().decode()
    if not ("P2" in type or "P5" in type):
        file.close()
        return None
    file.close()
    return type


def getAscii(filepath):
    file = open(filepath, 'r')
    file.readline()
    #skip comments
    while True:
        line = file.readline()
        if line[0] != '#': break
    # img width and length
    dimx, dimy = line.split()
    dimx, dimy = int(dimx), int(dimy)
    # NDG
    nivg = int(file.readline())
    # reading pixels
    imgMatrix = []
    for line in file.readlines():
        for num in line.split():
            imgMatrix.append(int(num))
    # verifying dimensions
    if len(imgMatrix) != dimx * dimy:
        file.close()
        return None, -1, -1, -1
    file.close()
    return imgMatrix, dimx, dimy, nivg


def getBinary(filepath):
    file = open(filepath, 'rb')
    file.readline()
    # skip comments
    while True:
        line = file.readline().decode()
        if line[0] != '#': break
    # img width and length
    dimx, dimy = line.split()
    dimx, dimy = int(dimx), int(dimy)

    nivg = int(file.readline().decode())
    imageread = []
    imageread = list(file.read(dimx * dimy))

    if len(imageread) != dimx * dimy:
        file.close()
        return None, -1, -1, -1
    file.close()
    return imageread, dimx, dimy, nivg


def write(filepath, image):
    data = utils.matrixToArray(image, s.height, s.width)
    writePGM(filepath, data)


def writePGM(filepath, image):
    # image is a tuple of (data,width,height,graylevel)
    file = open(filepath, "w")
    file.write("P2\n")
    file.write("#result img \n")
    file.write(str(s.width) + " " + str(s.height) + "\n")
    file.write(str(s.graylevel) + "\n")
    for num in range(0, len(image)):
        # file.write(str(num)+"\t")
        file.write(str(image[num]) + " ")
        if ((num + 1) % s.width == 0):
            file.write("\n")
    file.close()
