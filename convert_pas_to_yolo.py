import xml.etree.ElementTree as ET
import glob
import os
FOLDER = "/home/ericlab/tsuchida/annotation/real_label_img/HV8/labels_demo/*"
OUTPUT = "/home/ericlab/tsuchida/annotation/real_label_img/HV8/labels"
files = glob.glob(FOLDER)

for yes in files:
    print(yes)
    basename = os.path.splitext(os.path.basename(yes))[0]
   
    file = open(yes)
    tree = ET.parse(file)
    root = tree.getroot()

    all_list = []

    img_file = root.find('filename').text  # 画像ファイル名を取得

    for obj in root.iter('object'):
        cls = obj.find('name').text
        xmlbox = obj.find('bndbox')
        b = [int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text)]

        all_list.append([img_file] + b + [cls])
    with open(OUTPUT + "/" + basename + ".txt", mode='w') as f:
        f.write(all_list[0][5] + " " + str(all_list[0][1]) + " " + str(all_list[0][2]) + " " + str(all_list[0][3]) + " " + str(all_list[0][4]))
    print(all_list)