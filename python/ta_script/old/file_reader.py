import os 

# !/usr/bin/python 
print("hello")
f= open('/home/srijan/Documents/quarter3/481/homeworks/hw2/files.txt' , "r" )
file_names = f.read()

file_arr = file_names.split("\n")
file_arr_new = []
for cur in file_arr: 
    cur = cur.replace("HW2 - Markov Chain Gang_", "")
    cur =  cur.split('_')[0]
    if len(cur) !=0:
        file_arr_new.append(cur)
        os.mkdir(os.path.join("/home/srijan/Documents/quarter3/481/homeworks/hw2/final/organized/" , cur))
        print("created new folder " , cur)

print(file_arr_new)

