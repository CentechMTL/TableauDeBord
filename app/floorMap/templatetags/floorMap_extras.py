# coding: utf-8

from __future__ import division

from ast import literal_eval
from decimal import *

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name='monthly_cost_rate')
def monthly_cost_rate(surface, annual_cost_rate):
    surface = Decimal(surface or 0)
    annual_cost_rate = Decimal(annual_cost_rate or 0)
    return "{:.2f}".format(surface * annual_cost_rate / 12)


@register.filter(name='coords_list')
@stringfilter
def coords_list(value):
    lst_int = literal_eval(value)
    lst_string = ",".join(str(i) for i in lst_int)
    return lst_string


@register.filter(name='coords_shape')
@stringfilter
def coords_shape(value):
    lst_int = literal_eval(value)
    if len(lst_int) == 4:
        return 'rect'
    else:
        return 'poly'


@register.filter(name='room_thumbnail')
@stringfilter
def room_thumbnail(value):
    coords = literal_eval(value)

    if len(coords) == 4:
        coords = [
            coords[0], coords[1],
            coords[2], coords[1],
            coords[2], coords[3],
            coords[0], coords[3]
        ]

    coords = fit(coords, 140, 140)

    # coords = trim(coords)
    # coords = resize(coords)

    return ",".join(str(i) for i in coords)


def fit(coords, max_width, max_height):
    output = [''] * len(coords)

    min_x = coords[0]
    max_x = coords[0]
    min_y = coords[1]
    max_y = coords[1]

    # Find the boundaries of the shape
    for key, val in enumerate(coords):
        if key % 2 == 0:  # X value
            min_x = (val if val < min_x else min_x)
            max_x = (val if val > max_x else max_x)
        else:  # Y value
            min_y = (val if val < min_y else min_y)
            max_y = (val if val > max_y else max_y)

    shape_width = max_x - min_x
    shape_height = max_y - min_y

    # Figures rescale size for the shape
    ratio_x = max_width / shape_width
    ratio_y = max_height / shape_height

    if ratio_x < 1 or ratio_y < 1:
        rescale = (ratio_x if ratio_x < ratio_y else ratio_y)
    else:
        rescale = 1

    # Trim and resize the shape
    for key, val in enumerate(coords):
        if key % 2 == 0:  # X value
            output[key] = (val - min_x) * rescale  # Trim, rescale
            output[key] += (max_width - shape_width * rescale) / 2  # Center
        else:  # Y value
            output[key] = (val - min_y) * rescale  # Trim, rescale
            output[key] += (max_height - shape_height * rescale) / 2  # Center

        output[key] = int(output[key])

    return output
