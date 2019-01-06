from PIL import Image


class task:  # 一个图片放大任务
    id = 0
    pic = Image.new('RGB', (0, 0))
    result = Image.new('RGB', (0, 0))
    statue = 0  # 对象状态
    time = 0  # 创建时间

    def __init__(self, pic, id):
        self.id = id
        self.pic = pic
        self.statue = 0
        self.time = 0

    def proceed(self, multiple=2, noise=0):  # 将这个对象提交并且尝试放大，返回是否提交成功
        pass

    def getdown(self):  # 从云端取回这个对象为图片对象
        pass
