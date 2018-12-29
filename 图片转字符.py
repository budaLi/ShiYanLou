#-*-coding:utf8-*-
#author : Lenovo
#date: 2018/12/29
from PIL import Image
import argparse


#首先 构建命令行输入参数处理  定义ArgumentParser实例
parser=argparse.ArgumentParser()

#定义输入文件 输出文件 输出字符画的宽和高
parser.add_argument("file") #输入文件
parser.add_argument("-o","--output")    #输出文件
parser.add_argument("--width",type=int,default=80)
parser.add_argument("--height",type=int,default=80)

#解析并获取参数
args=parser.parse_args()

#输入的图片文件路径
img=args.file

#输出字符画的宽度
width=args.width

height=args.height

output=args.output

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


#Rgb值转字符 alpha为0时表示图片中该位置为空白
def get_char(r,g,b,alpha=256):

    if alpha==0:
        return " "

    #获取字符集的长度
    length=len(ascii_char)

    #将RGB值转为灰度值 灰度值范围为0-25
    gray=int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    #灰度值范围为0-255 而字符集只有70  需要进行如下处理才能将灰度值映射到指定的字符上

    unit=(256.0+1)/length

    #返回灰度值对应的字符
    return ascii_char[int(gray/unit)]


if __name__=="__main__":

    #打开并调整图片的宽和高
    im=Image.open(img)
    im=im.convert("RGB")        #没有这一行无法运行
    im=im.resize((width,height),Image.NEAREST)
    #初始化输出的字符串
    txt=""

    #遍历图片中的每一行
    for i in range(height):
        for j in range(width):
            txt += get_char(*im.getpixel((j,i)))

        txt+="\n"

    print(txt)


    #字符画输出到文件
    if output:
        with open(output,"w") as f:
            f.write(txt)
    else:
        with open("output.txt","w") as f:
            f.write(txt)




