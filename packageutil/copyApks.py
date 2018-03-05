
# 拷贝各个渠道的apk到统一的包的类
import os
import shutil

root_pack_dir = "E:\package"

# for r in os.listdir(root_pack_dir):
#     print(r)

def searchApk(packagePath):
    # 是否是文件夹
    if os.path.isdir(packagePath):
         # 是文件夹的话便利一下当前文件夹的目录
        for file in os.listdir(packagePath):
            file = packagePath+"\\"+file
            if os.path.isdir(file):
                # 如果还是目录的话，递归
                searchApk(file)
            else:
                if (".apk" in file):
                    print("apk的名字：%s"%file)
                    # 开始复制
                    shutil.copyfile(file,"E:\\finishpackage\\"+os.path.basename(file))

searchApk(root_pack_dir)