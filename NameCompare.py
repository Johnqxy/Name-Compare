import os

filePath1 = r'/home/boyd/yolo3-tf2-main/VOCdevkit/VOC2007/JPEGImages'
filePath2 = r'/home/boyd/yolo3-tf2-main/VOCdevkit/VOC2007/labels'

# list1 = os.listdir(filePath1)
# file_list1 = [] #annotations中的文件名列表 不带后缀
# for i in list1:
#     file_list1.append(os.path.splitext(i)[0])
# # print(file_list1)
#
# list2 = os.listdir(filePath2)
# file_list2 = [] #image中的文件名列表 不带后缀
# for i in list2:
#     file_list2.append(os.path.splitext(i)[0])
# # print(file_list2)
# #找出没有标注的图片名称列表
# b = [y for y in file_list2 if y not in file_list1]
# #把这些列表加上扩展名 然后将其删除
# path = r'/home/boyd/yolo3-tf2-main/VOCdevkit/VOC2007/JPEGImages'
# for i in b:
#     os.remove(os.path.join(path, i+'.jpg'))
list1 = os.listdir(filePath1)
print(len(list1))
file_list1 = [] #annotations中的文件名列表 不带后缀
for i in list1:
    file_list1.append(os.path.splitext(i)[0])
# print(file_list1)

list2 = os.listdir(filePath2)
print(len(list2))
file_list2 = [] #image中的文件名列表 不带后缀
for i in list2:
    file_list2.append(os.path.splitext(i)[0])
# print(file_list2)
#找出没有标注的图片名称列表
b = [y for y in file_list1 if y not in file_list2]
#把这些列表加上扩展名 然后将其删除
path = r'/home/boyd/yolo3-tf2-main/VOCdevkit/VOC2007/JPEGImages'
for i in b:
    os.remove(os.path.join(path, i+'.jpg'))
