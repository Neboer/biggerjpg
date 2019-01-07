from PIL import Image


class task:  # 一个图片放大任务
    index = None  # 该任务的索引
    pic = None
    result = None
    statue = 0  # 对象状态，0表示转换中，1表示转换完成，-1表示转换错误
    time = 0  # 创建时间

    def __init__(self, pic, index):
        self.index = index
        self.pic = pic
        self.statue = 0
        self.time = 0

    def proceed(self, multiple=2, noise=0):  # 将这个对象提交并且尝试放大，返回是否提交成功
        self.statue = 0
        pass

    def getdown(self):  # 从云端取回这个对象为图片对象，成功则返回图片对象，不成功就返回NULL
        # 每次调用都查询并改变转换状态
        self.statue = 1
        pass
