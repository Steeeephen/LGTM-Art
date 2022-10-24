import os
import sys
from typing import List, Any, Tuple

import cv2
import numpy as np


def read_image(file_path: str,
               img_width: int,
               img_height: int) -> Tuple[np.array, np.array]:
    """
    Read image from filepath and parse contours

    Parameters
    ----------
    file_path : str
        Path to image
    img_width : int
        Width to resize image to
    img_height : int
        Height to resize image to

    Returns
    -------
    img : np.array
        Image loaded from filepath
    contours : np.array
        Contours of the image
    """
    img = cv2.imread(file_path)

    img = cv2.resize(
        img, 
        (img_width, img_height), 
        interpolation = cv2.INTER_AREA
    )

    img_gray = cv2.cvtColor(
        img, 
        cv2.COLOR_BGR2GRAY
    )

    _, thresh = cv2.threshold(
        img_gray,
        0,
        255,
        cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
    )

    contours, _ = cv2.findContours(
        thresh,
        cv2.RETR_TREE,
        cv2.CHAIN_APPROX_NONE
    )

    return img, contours

def shift(seq: List[Any]) -> List[Any]:
    """
    Shift list values by 1

    Parameters
    ----------
    seq : List[Any]
        List to shift values

    Returns
    -------
    seq : List[any]
        List with shifted values
    """
    seq = seq[1:] + seq[:1]

    return seq[-1], seq

def print_lgtm(file_path: str,
               img_height: int = 40,
               img_width: int = 80) -> None:
    """
    Print the letters LGTM in the shape of an image

    Parameters
    ----------
    file_path : str
        Path to input image
    img_height : int
        Shrink image to this height for output
    img_width : int
        Shrink image to this width for output
    """
    img, contours = read_image(
        file_path=file_path,
        img_width=img_width,
        img_height=img_height
    )

    # Create blank canvas
    canvas = np.zeros(img.shape[:2]).astype(str)

    # Replace 0 with 1 in shape of contours
    for contour in contours:
        for point in contour:
            canvas[point[0][1], point[0][0]] = 1

    canvas = canvas[:,1:-1]

    letter = 'l'
    letters = ['g', 't', 'm', 'l']

    for j, row in enumerate(canvas):
        for i, val in enumerate(row):
            if val == "1":
                canvas[j][i] = letter
                letter, letters = shift(letters)

    # Replace 0 with whitespace
    image_with_whitespace = np.where(canvas == '0.0', ' ', canvas)

    # Print contours in clean way
    clean_image_with_whitespace = '\n'.join([''.join(row) for row in image_with_whitespace])

    print(clean_image_with_whitespace)

def cli():
    print_lgtm(sys.argv[1])

if __name__=='__main__':
    cli()