# !/usr/bin/python 

import os 
import shutil 
import datetime 
import numpy as np 
penalty = [] 

folder = './data'
def start():
    for root, dirs, files in os.walk(folder , topdown=False): 
        for f in files:
            if "txt" in f: 
                file_path = os.path.join(root , f)
                cur_file = open(file_path, "r")
                text = cur_file.read()
                lines = text.split("\n")
                find_penalty(lines[0], lines[2])

    
    late_ds = np.array(penalty)
    late_condition= late_ds[:,2] == 'late'
    late_stu = late_ds[late_condition]
    np.savetxt("./rr_late.csv" , late_stu , delimiter = ",",  fmt='%s')
    print("save complete...")

def find_penalty(heading, time_text): 
    user_name = heading[heading.find("(") +1 : heading.find(")")-1]
    date_str = time_text[time_text.find(":")+2:]
    sub_window = "Thursday, April 30, 2020 11:59:59 PM EDT"
    date_format = "%A, %B %d, %Y %I:%M:%S %p %Z"
    submission_date = datetime.datetime.strptime(date_str, date_format)
    actual_date = datetime.datetime.strptime(sub_window, date_format)
    lateness =""
    if submission_date > actual_date:  
       lateness = "late"  
       print(user_name , " " , date_str , " " , lateness)
    penalty.append([user_name , date_str ,lateness])

    
if __name__ == "__main__":
    start()    
"""
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
"""
