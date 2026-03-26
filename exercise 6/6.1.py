def rectangle_area(length, width = None):
    if width is None:
        width = length;
    return length*width;
print(rectangle_area(6));