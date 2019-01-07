from PIL import Image
from cubu import cutpic, build
from bjpost import task
from twodbar import bar


def push(name):
    r = []
    img = Image.open(name)
    s = cutpic(img)
    for co, tu in s.items():
        a = task(tu, co)
        while a.proceed() == 0:  # 提交不成功，反复提交直到成功
            pass
        r.append(a)
    return r


def get(r):  # 此方法从云端尝试下载图片所有部分，可以写为图形界面，提供每个部分下载进度的实时反馈。这个实现是在控制台中用方块表示下载的进度
    x = 0
    y = 0
    b = {}
    for a in r:
        if a.index[0] > x: x = a.index[0]
        if a.index[1] > y: y = a.index[1]
    ba = bar((x, y))
    ba.show()
    while True:
        for mission in r:
            if mission.statue == -1:
                pass  # 处理错误
                continue
            if mission.statue == 0 and mission.getdown() is not None:
                b[mission.index] = mission.result
                ba.update(mission.index)
                ba.show()
