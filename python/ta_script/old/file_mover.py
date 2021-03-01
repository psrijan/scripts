# !/usr/bin/python 

import os 
import shutil 
root_fol = "/home/srijan/Documents/quarter3/481/homeworks" 

f= open('/home/srijan/Documents/quarter3/481/homeworks/hw2/files.txt' , "r" )
file_names = f.read()
file_arr = file_names.split("\n")
file_arr_new = []
for cur in file_arr: 
    cur = cur.replace("HW2 - Markov Chain Gang_", "")
    cur =  cur.split('_')[0]
    if len(cur) !=0:
        file_arr_new.append(cur)

print(file_arr_new)


 
for root, dirs, files in os.walk(root_fol + "/hw2/final" , topdown = False): 
    for cur_file in files: 
        cur_file_path = os.path.join(root, cur_file)
        for dir_name in file_arr_new:
            if dir_name in cur_file_path: 
                print("%s is in folder %s" %(cur_file_path, dir_name)) 
                try: 
                    shutil.move(cur_file_path , os.path.join(root_fol+"/hw2/final/organized/" + dir_name, cur_file))       
                    print("moved")
                except: 
                    print("file error")
                

