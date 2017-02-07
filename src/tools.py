import pygame as pg

def split_sheet(sheet, size, dims):
    """
    Divide a loaded sprite sheet into subsurfaces.
    
    The argument size is the width and height of each frame (w,h)
    columns and rows are the integer number of cells horizontally and
    vertically.
    """
    subsurfaces = []
    for y in range(dims[1]):
        row = []
        for x in range(dims[0]): 
            rect = pg.Rect((x*size[0], y*size[1]), size)
            row.append(sheet.subsurface(rect))
        subsurfaces.append(row)
    return subsurfaces
