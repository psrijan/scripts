# !/usr/bin/python 

import os 
import shutil 
root_fol = "/home/srijan/Documents/quarter3/481/homeworks" 

f = open(root_fol + "/names1.txt" , "r") 
file_val  = f.read() 
print(file_val)
file_names = file_val.split("\n");  

file_dict = {} 
for fn in file_names: 
   file_dict[fn] = root_fol+"/hw2/origanized/" + fn  
print (file_names)

 
for root, dirs, files in os.walk(root_fol + "/hw2" , topdown = False): 
    for cur_file in files: 
        cur_file_path = os.path.join(root, cur_file)
        for dir_name in file_names:
            if dir_name in cur_file_path: 
                print("%s is in folder %s" %(cur_file_path, dir_name)) 
                try: 
                    shutil.move(cur_file_path , os.path.join(root_fol+"/hw2/organized/" + dir_name, cur_file))       
                    print("moved")
                except: 
                    print("file error")

