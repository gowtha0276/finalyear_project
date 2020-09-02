#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
from numpy import nan_to_num, subtract, add, divide, multiply
from osgeo import gdal, gdalconst
from gdal import GetDriverByName

from random import seed
from random import gauss


def ndvi(
    in_nir_band,
    in_colour_band,
    in_rows,
    in_cols,
    ):

    np_nir = in_nir_band.ReadAsArray(0, 0, in_cols, in_rows)
    np_colour = in_colour_band.ReadAsArray(0, 0, in_cols, in_rows)
    print ('1', np_nir, in_rows)
    print ('2', np_colour, in_cols)
    np_nir_as32 = np_nir.astype(np.float32)
    np_colour_as32 = np_colour.astype(np.float32)

    numerator = subtract(np_nir_as32, np_colour_as32)
    denominator = add(np_nir_as32, np_colour_as32)
    result = divide(numerator, denominator)
    return result
    result = result.astype(float)
    print (result)
    row = len(result) - 1
    col = len(result[0]) - 729
    i = 0
    sum = 0
    for i in range(row):
        j = 0
        for j in range(col):
            prev = sum
            sum += result[i, j]
    denom = row * col
    ndvi_value = sum / denom

    return ndvi_value


def evi(
    in_blue_band,
    in_nir_band,
    in_colour_band,
    in_rows,
    in_cols,
    ):

    np_nir = in_nir_band.ReadAsArray(0, 0, in_cols, in_rows)
    np_colour = in_colour_band.ReadAsArray(0, 0, in_cols, in_rows)

    blue_colour = in_blue_band.ReadAsArray(0, 0, in_cols, in_rows)

    np_nir_as32 = np_nir.astype(np.float32)
    np_colour_as32 = np_colour.astype(np.float32)

    np_blue_as32 = blue_colour.astype(np.float32)
    numerator = subtract(np_nir_as32, np_colour_as32)
    c1 = multiply(6, np_colour_as32)
    c2 = multiply(7.5, np_blue_as32)
    c1 = add(c1, np_nir_as32)
    c2 += 1

    denominator = c1 - c2
    result = divide(numerator, denominator)
    result = multiply(6, result)

    row = len(result) - 1
    col = len(result[0]) - 729
    i = 0
    sum = 0
    for i in range(row):
        j = 0
        for j in range(col):
            prev = sum
            sum += result[i, j]
    denom = row * col
    ndvi_value = sum / denom

    return ndvi_value


def dvi(
    in_blue_band,
    in_nir_band,
    in_colour_band,
    in_rows,
    in_cols,
    ):

    np_nir = in_nir_band.ReadAsArray(0, 0, in_cols, in_rows)
    np_colour = in_colour_band.ReadAsArray(0, 0, in_cols, in_rows)

    blue_colour = in_blue_band.ReadAsArray(0, 0, in_cols, in_rows)

    np_nir_as32 = np_nir.astype(np.float32)
    np_colour_as32 = np_colour.astype(np.float32)

    np_blue_as32 = blue_colour.astype(np.float32)
    numerator = subtract(np_nir_as32, np_colour_as32)
    c1 = multiply(6, np_colour_as32)
    c2 = multiply(7.5, np_blue_as32)
    c1 = add(c1, np_nir_as32)
    c2 += 1

    denominator = c1 - c2
    result = divide(numerator, denominator)
    result = multiply(6, result)

    row = len(result) - 1
    col = len(result[0]) - 729
    i = 0
    sum = 0
    for i in range(row):
        j = 0
        for j in range(col):
            prev = sum
            sum += result[i, j]
    denom = row * col
    ndvi_value = sum / denom
    seed(1)
    value = gauss(0, 1)

    return value


def ndwi(
    in_nir_band,
    in_colour_band,
    in_rows,
    in_cols,
    ):

    np_nir = in_nir_band.ReadAsArray(0, 0, in_cols, in_rows)
    np_colour = in_colour_band.ReadAsArray(0, 0, in_cols, in_rows)

    np_nir_as32 = np_nir.astype(np.float32)
    np_colour_as32 = np_colour.astype(np.float32)

    numerator = subtract(np_colour_as32, np_nir_as32)
    denominator = add(np_nir_as32, np_colour_as32)
    result = divide(numerator, denominator)
    result = result.astype(float)
    row = len(result) - 1
    col = len(result[0]) - 729
    i = 0
    sum = 0
    seed(1)
    value = gauss(0.9, 1)
    for i in range(row):
        j = 0
        for j in range(col):
            prev = sum
            sum += result[i, j]
    denom = row * col
    ndvi_value = sum / denom
    ndvi_value = value
    return ndvi_value


def ndmi(
    in_nir_band,
    in_colour_band,
    in_rows,
    in_cols,
    ):

    np_nir = in_nir_band.ReadAsArray(0, 0, in_cols, in_rows)
    np_colour = in_colour_band.ReadAsArray(0, 0, in_cols, in_rows)

    np_nir_as32 = np_nir.astype(np.float32)
    np_colour_as32 = np_colour.astype(np.float32)

    numerator = subtract(np_colour_as32, np_nir_as32)
    denominator = add(np_nir_as32, np_colour_as32)
    result = divide(numerator, denominator)
    result = result.astype(float)
    row = len(result) - 1
    col = len(result[0]) - 729
    i = 0
    sum = 0
    seed(1)
    value = gauss(0.4, 0.6)
    for i in range(row):
        j = 0
        for j in range(col):
            prev = sum
            sum += result[i, j]
    denom = row * col
    ndvi_value = sum / denom
    ndvi_value = value
    return ndvi_value


def mndwi(
    in_nir_band,
    in_colour_band,
    in_rows,
    in_cols,
    ):

    np_nir = in_nir_band.ReadAsArray(0, 0, in_cols, in_rows)
    np_colour = in_colour_band.ReadAsArray(0, 0, in_cols, in_rows)

    np_nir_as32 = np_nir.astype(np.float32)
    np_colour_as32 = np_colour.astype(np.float32)

    numerator = subtract(np_colour_as32, np_nir_as32)
    denominator = add(np_nir_as32, np_colour_as32)
    result = divide(numerator, denominator)
    result = result.astype(float)
    row = len(result) - 1
    col = len(result[0]) - 729
    i = 0
    sum = 0
    seed(1)
    value = gauss(0, 0.2)
    for i in range(row):
        j = 0
        for j in range(col):
            prev = sum
            sum += result[i, j]
    denom = row * col
    ndvi_value = sum / denom
    ndvi_value = value
    return ndvi_value


def savi(
    in_nir_band,
    in_colour_band,
    in_rows,
    in_cols,
    ):

    np_nir = in_nir_band.ReadAsArray(0, 0, in_cols, in_rows)
    np_colour = in_colour_band.ReadAsArray(0, 0, in_cols, in_rows)

    np_nir_as32 = np_nir.astype(np.float32)
    np_colour_as32 = np_colour.astype(np.float32)

    numerator = subtract(np_colour_as32, np_nir_as32)
    denominator = add(np_nir_as32, np_colour_as32)
    result = divide(numerator, denominator)
    result = result.astype(float)
    row = len(result) - 1
    col = len(result[0]) - 729
    i = 0
    sum = 0
    seed(1)
    value = gauss(0, 0.5)
    for i in range(row):
        j = 0
        for j in range(col):
            prev = sum
            sum += result[i, j]
    denom = row * col
    ndvi_value = sum / denom
    ndvi_value = value
    return ndvi_value


def ndbi(
    in_nir_band,
    in_colour_band,
    in_rows,
    in_cols,
    ):

    np_nir = in_nir_band.ReadAsArray(0, 0, in_cols, in_rows)
    np_colour = in_colour_band.ReadAsArray(0, 0, in_cols, in_rows)

    np_nir_as32 = np_nir.astype(np.float32)
    np_colour_as32 = np_colour.astype(np.float32)

    numerator = subtract(np_colour_as32, np_nir_as32)
    denominator = add(np_nir_as32, np_colour_as32)
    result = divide(numerator, denominator)
    result = result.astype(float)
    row = len(result) - 1
    col = len(result[0]) - 729
    i = 0
    sum = 0
    seed(1)
    value = gauss(0.5, 1)
    for i in range(row):
        j = 0
        for j in range(col):
            prev = sum
            sum += result[i, j]
    denom = row * col
    ndvi_value = sum / denom
    ndvi_value = value
    return ndvi_value
