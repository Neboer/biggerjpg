from PIL import Image


def cutpic(img, size=3000):  # size in px,return a dict including tuple to img
    c = {}
    ax = int(img.size[0] / size)
    if img.size[0] % size == 0: ax -= 1
    ay = int(img.size[1] / size)
    if img.size[1] % size == 0: ay -= 1
    for y in range(0, ay):
        for x in range(0, ax):
            c[(x, y)] = img.crop((x * size, y * size, (x + 1) * size, (y + 1) * size))
        c[(ax, y)] = img.crop((ax * size, y * size, img.size[0], (y + 1) * size))
    for x in range(0, ax):
        c[(x, ay)] = img.crop((x * size, ay * size, (x + 1) * size, img.size[1]))
    c[(ax, ay)] = img.crop((ax * size, ay * size, img.size[0], img.size[1]))
    return c


def build(c):  # c is a dict,like above
    unit = c[(0, 0)]
    xsize = 0
    ysize = 0
    for tu in c.keys():
        if tu[0] > xsize: xsize = tu[0]
        if tu[1] > ysize: ysize = tu[1]
    img = Image.new(unit.mode, (xsize * unit.size[0] + c[(xsize, 0)].size[0],
                                ysize * unit.size[1] + c[(0, ysize)].size[1]))
    for co, tu in c.items():
        x1 = unit.size[0] * co[0]
        y1 = unit.size[1] * co[1]
        img.paste(tu, (x1, y1))
    return img
