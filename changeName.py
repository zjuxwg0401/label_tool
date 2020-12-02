import os

path = "/Users/shallwego2/Pictures/seq10/"

for frame_num in range(0,251):
    old_file_name = path + "frame" + "{0:04d}".format(2*frame_num) + ".jpg"
    new_file_name = path + "frame"  + "{0:04d}".format(frame_num) + ".jpgcd "
    os.rename(old_file_name,new_file_name)
