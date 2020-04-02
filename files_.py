import os


# 遍历文件夹
def walkFile(file):
    
    for root, dirs, files in os.walk(file):

        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list

        # 遍历文件
        for f in files:
            print(f)

        # # 遍历所有的文件夹
        # for d in dirs:
        #     print(os.path.join(root, d))


def main():
    walkFile("./image")


if __name__ == '__main__':
    main()