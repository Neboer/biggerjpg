import os


class bar:  # 创建一个二维进度条
    x_max = 0
    y_max = 0
    list = {}

    def __init__(self, xsize, ysize):  # size是一个元组，(行,列)（从1开始）
        self.x_max = xsize
        self.y_max = ysize

    def show(self):
        for y in range(1, self.y_max + 1):
            for x in range(1, self.x_max + 1):
                if (x, y) in self.list.keys():
                    print(u"■", end='')
                else:
                    print(u"□", end='')
            print("")

    def update(self, coord):
        self.list[coord] = 1

