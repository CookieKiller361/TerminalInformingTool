import os
import pandas as pd
import csv

#i want to implement a function like that directly in the setup_locaten function
def save_data_create(file_location,filename,data):
    #checks witch file system is used
    if os.name('nt'):
        full_path=file_location+"\\"+filename
    else:
        full_path=file_location+"/"+filename
    #checks if the file exists
    
    if os.path.exists(full_path):
        '''
        search_data_csv(full)
        '''
        file=open(full_path,"a")
        file
    else:
        file=open(full_path,'w')
        file.write(data)
        file.close
    
    def search_data_csv(filepath,search_for):
        data=pd.read_csv(filepath)
        file=open(filepath,"r")
        csv_reader=csv.reader(file)
        for row in csv_reader:
            if search_for in row:
                return(row)
