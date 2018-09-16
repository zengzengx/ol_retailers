import random, string
import hashlib
import hmac

from PIL import Image, ImageFont, ImageFilter, ImageDraw


def hash_md5(value, salt=None):
    md5 = hashlib.md5(value.encode("utf-8"))
    if salt is not None:
        md5.update(salt.encode("utf-8"))
    return md5.hexdigest()


def hmac_md5(value, salt=None):
    md5 = hmac.new(value.encode("utf-8"), salt.encode("utf-8"), "MD5")
    return md5.hexdigest()


def getRandomChar(count=4):
    # 生成随机字符串
    # string 模块包含各种字符串，以下为小写字母加数字
    ran = string.ascii_lowercase + string.digits
    char = ''
    for i in range(count):
        char += random.choice(ran)
    return char


# 返回一个随机的 RGB 颜色
def getRandomColor():
    return (random.randint(50, 150), random.randint(50, 150), random.randint(50, 150))


def create_code():
    # 创建图片，模式，大小，背景色
    img = Image.new('RGB', (120, 30), (255, 255, 255))
    # 创建画布
    draw = ImageDraw.Draw(img)
    # 设置字体
    font = ImageFont.truetype('arial.ttf', 25)

    code = getRandomChar()
    # 将生成的字符画在画布上
    for t in range(4):
        draw.text((30 * t + 5, 0), code[t], getRandomColor(), font)

        # 生成干扰点
    for _ in range(random.randint(0, 50)):
        # 位置，颜色
        draw.point((random.randint(0, 120),
                    random.randint(0, 30)), fill=getRandomColor())

        # 使用模糊滤镜使图片模糊
    img = img.filter(ImageFilter.CONTOUR)
    # 保存
    # img.save(''.join(code)+'.jpg','jpeg')
    return img, code