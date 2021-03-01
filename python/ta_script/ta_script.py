import datetime 
import os
import shutil 
import re 

config = {} 
config["root"] = "/home/srijan/Documents/quarter\ 5/SE320/assignment0/"
print(config["root"])

def create_individual_dirs(): 
    file_names =[]
    os.chdir(config["root"])
   #os.makedirs("organized")
    for root,  dirs , files in  os.walk(config["root"]):
        for cur in files: 
            if ".txt" in cur: 
                cur = cur.replace("HW4 - Markov\'s Decisions_", "")
                cur =  cur.split('_')[0]
                print(cur)
                if len(cur) !=0:
                    file_names.append(cur)
                    # try: 
                        # #os.mkdir(os.path.join(config["root"] , "organized/" + cur))
                    # except: 
                        # print("some error occured")
                    # print("created new folder " , cur)


    print(len(file_names))
    return file_names

def get_folder_name(cur, folder_names): 
    for folder in folder_names: 
        if folder in cur: 
            return folder
    return ""


def copy_files(folder_names): 
    for root, dirs, files in os.walk(config["root"]):
        for cur in files: 
            folder_name = get_folder_name(cur , folder_names) 
            if (folder_name != ""):
                dest = os.path.join(config["root"], "organized" , folder_name , cur)
                shutil.move(os.path.join( root , cur) , dest)  
                print("move complete")


def find_penalty(heading, time_text):                                           
    user_name = heading[heading.find("(") +1 : heading.find(")")-1]             
    date_str = time_text[time_text.find(":")+2:]                                
    print("date %s \n" %(date_str))
    sub_window = "Tuesday, June 2, 2020 11:59:59 PM EDT"                     
    date_format = "%A, %B %d, %Y %I:%M:%S %p %Z"                                
    print("submitted date: %s" %date_str)
    submission_date = datetime.datetime.strptime(date_str.strip(), date_format)         
    actual_date = datetime.datetime.strptime(sub_window, date_format)           
    lateness =""                                                                
    if submission_date > actual_date:                                           
       lateness = "late"                                                        
       print(user_name , " " , date_str , " " , lateness)                       
       return [user_name , date_str ,lateness]
                                                                 

def calc_lateness(folder_names): 
    penalty_list = []

    for i, folder in enumerate(folder_names): 
        print(i)
        student_folder = os.path.join(config["root"] , "organized",  folder)
        os.chdir(student_folder)
        file_listing = os.listdir()

        cur_dir = os.getcwd()
        for cur in file_listing: 
            if ("HW4 - Markov\'s Decisions_"in cur) and (".txt" in cur): 
                meta_file = open(os.path.join(cur_dir, cur) , "r") 
                txt = meta_file.read()
                txt_arr = txt.split("\n")
                penalty = find_penalty(txt_arr[0] , txt_arr[2])
                if penalty != None: 
                    penalty_list.append(penalty)
    print(penalty_list)
    f = open(config['root'] + '/hw4_late.txt' , 'w') 
    w_str = '';
    for row in penalty_list: 
        w_str+= ''.join(row) + "\n"
    f.write(w_str)
    f.close()
    return penalty_list 

if __name__ == "__main__": 
    folder_names = create_individual_dirs()
    copy_files(folder_names)
    f = open(config['root'] + '/' + 'files.txt' , 'r') 
    f_text = f.read() 
    folder_names = f_text.split('\n') 
    print(folder_names)
    calc_lateness(folder_names)


