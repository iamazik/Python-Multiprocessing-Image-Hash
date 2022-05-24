# https://pyimagesearch.com/2019/09/09/multiprocessing-with-opencv-and-python/

import cv2
import pickle
import numpy as np


def dhash(image, hashSize=8):
    # convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # resize the input image, adding a single column (width) so we
    # can computer the horizontal gradient
    resized = cv2.resize(gray, (hashSize+1, hashSize))

    # compute the (relative) horizontal gradient between adjacent
    # column pixel
    diff = resized[:, 1:] > resized[:, :-1]

    # convert the difference image to a has
    return sum([2**i for(i, v) in enumerate(diff.flatten()) if v])


def convert_hash(h):
    # convert the hash to NumPy's 64-bit float and then back to
    # Python's built in int
    return int(np.array(h, dtype="float64"))


'''
@param: l: list of elements (in this case, file paths)
@param: n: number of n-sized chunks to generate
'''


def chunk(l, n):
    # loop over the list in n-sized chunks
    for i in range(0, len(l), n):
        # yield the current n-sized chunk to the calling function
        yield l[i: i+n]


def process_images(payload):
    # display the process ID for debugging and initialize the hashes
    # dictionary
    print("[INFO] starting process {}".format(payload["id"]))
    hashes = {}

    # loop over the image paths
    for imagePath in payload["input_paths"]:
        # load the input image, compute the hash, and convert it
        image = cv2.imread(imagePath)
        h = dhash(image)
        h = convert_hash(h)

        # update the hashes dictionary
        l = hashes.get(h, [])
        l.append(imagePath)
        hashes[h] = l

    # serialize the hashes dictionary to disk using supplied
    # output path
    print("[INFO] process {} serializing hashes".format(payload["id"]))
    f = open(payload["output_path"], "wb")
    f.write(pickle.dumps(hashes))
    f.close()
