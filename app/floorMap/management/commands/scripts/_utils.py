# coding: utf-8

from math import factorial


def combinations_count(n, r):
    return int(factorial(n) / (factorial(n - r) * factorial(r)))


def rect_to_poly(x1, y1, x2, y2):
    """
    Transforms a rectangle list into a polygon list
    :param x1: Top left x coordinate
    :param y1: Top left y coordinate
    :param x2: Bottom right x coordinate
    :param y2: Bottom right y coordinate
    :return: Equivalent to received parameters but
    """
    return x1, y1, x2, y1, x2, y2, x1, y2


def boundary_box(*coords):
    """
    Rearranges coordinates to return a rectangular boundary
        around the coordinates
    The first 2 values will ALWAYS the top left point
    :param coords:
    :return: list of 4 integers representing the boundary rectangle
    """
    # initializes box with initial point : box[minX, minY, maxX, maxY]
    bbox = [coords[0], coords[1], coords[0], coords[1]]

    # Skips initial point and searches for greater or smaller values
    for i in range(2, len(coords)):
        val = coords[i]

        if i % 2 == 0:  # X value
            bbox[0] = (val if val < bbox[0] else bbox[0])  # found a new X min
            bbox[2] = (val if val > bbox[2] else bbox[2])  # found a new X max
        else:  # Y value
            bbox[1] = (val if val < bbox[1] else bbox[1])  # found a new Y min
            bbox[3] = (val if val > bbox[3] else bbox[3])  # found a new X max

    return bbox[0], bbox[1], bbox[2], bbox[3]
