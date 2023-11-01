import cv2
import numpy as np

def convert_coord(coord_list):
    x_min, x_max, y_min, y_max = coord_list
    return [[x_min, y_min], [x_max, y_min], [x_max, y_max], [x_min, y_max]]

# https://www.life2coding.com/cropping-polygon-or-non-rectangular-region-from-image-using-opencv-python/
# https://stackoverflow.com/questions/48301186/cropping-concave-polygon-from-image-using-opencv-python
def crop(image, points):
    pts = np.array(points, np.int32)

    # Crop the bounding rect
    rect = cv2.boundingRect(pts)
    x,y,w,h = rect
    croped = image[y:y+h, x:x+w].copy()

    # make mask
    pts = pts - pts.min(axis=0)

    mask = np.zeros(croped.shape[:2], np.uint8)
    cv2.drawContours(mask, [pts], -1, (255, 255, 255), -1, cv2.LINE_AA)

    # do bit-op
    dst = cv2.bitwise_and(croped, croped, mask=mask)

    # add the white background
    bg = np.ones_like(croped, np.uint8) * 255
    cv2.bitwise_not(bg,bg, mask=mask)
    result = bg + dst

    return result
