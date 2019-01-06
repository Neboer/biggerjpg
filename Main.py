from PIL import Image
from cubu import cutpic, build
from bjpost import task

img = Image.open("Flag.png")
s = cutpic(img)
id = 0
for co, tu in s.items():
    id += 1
    a = task(tu, id)
    while a.proceed() == 0:  # 提交不成功
        pass
