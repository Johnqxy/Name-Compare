import os
paths='/home/boyd/coco_only_person/images/train/'
f=open('/home/boyd/coco_only_person/images/train.txt','r+')
filenames=os.listdir(paths)
for filename in filenames:
    if os.path.splitext(filename)[1]=='.jpg':
        out_path="/home/boyd/coco_only_person/images/train/"+filename
        print(out_path)
        #f.writable(out_path+'\n')
        f.write(out_path+'\n')
f.close()