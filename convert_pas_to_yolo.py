import xml.etree.ElementTree as ET
import glob
import os
import numpy as np
FOLDER = "/home/ericlab/tsuchida/2022_07/annotation/real_data_t_pipe_ano_again/label_temp/*"
OUTPUT = "/home/ericlab/tsuchida/2022_07/annotation/real_data_t_pipe_ano_again/labels"
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
        # print([img_file] + b + [cls])
    # print(np.array(all_list).shape)
    # print(all_list)
    with open(OUTPUT + "/" + basename + ".txt", mode='w') as f:
        for i in range(np.array(all_list).shape[0]):
            f.write(all_list[i][5] + " " + str(all_list[i][1]) + " " + str(all_list[i][2]) + " " + str(all_list[i][3]) + " " + str(all_list[i][4]) + "\n")
    # print(all_list)