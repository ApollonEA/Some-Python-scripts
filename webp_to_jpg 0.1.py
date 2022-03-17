import os
import datetime

import imghdr
from PIL import Image

cur_dir = os.getcwd()

inp_folder_name = input("Type the name of folder where your .webp images are (don't forget to put scripr and folder with images in the same directory)")
picture_list = os.listdir(inp_folder_name)


cur_time = datetime.datetime.now()
#print(cur_time)
curtime_str = str(cur_time).split(" ")
#print(curtime_str)
curtime_hh_mm_ss = curtime_str[1].split(".")[0]
curtime_ready = curtime_hh_mm_ss.split(":")[0] + "_" + curtime_hh_mm_ss.split(":")[1] + "_" + curtime_hh_mm_ss.split(":")[2]
#print("curtime_ready " + curtime_ready)


out_folder_name = cur_dir + "\\out_pics" + curtime_ready

os.makedirs(out_folder_name)


for index, picture_name in enumerate(picture_list):
    im = Image.open(cur_dir + "\\inp_pics\\" + picture_name).convert("RGB")
    im.save(out_folder_name + "\\" + picture_name.split(".")[0]+".jpg","jpeg")
    
print(f"Convertion completed. I converted {index+1} .webp images to .jpg")    
