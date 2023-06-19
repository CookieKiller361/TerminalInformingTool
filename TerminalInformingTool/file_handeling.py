import os
import pandas as pd

def relative_path(filepath):
    current_directory = os.getcwd()
    fullpath=current_directory+filepath
    return fullpath

def filesystem(filepath):
    filepath=relative_path(filepath)
    if os.name == 'nt':
        filepath_changed=filepath.replace("/","\\")
        return filepath_changed
    else:
        return filepath

def check_if_exist(filepath):
    if os.path.exists(filepath):
        return True
    else:
        return False

#header_data=['data_from','data']
def csv_file_frame_create(filepath,header_data=None):
    #creates a DataFrame from the data given within the header of the function
    df = pd.DataFrame([header_data])
    #saves the csv file with the data from the function header as header for the csv file
    df.to_csv(filepath, index=False, header=False)


def csv_file_add_data(filepath,data):
    file=open(filepath,'a')
    for key, value in data.items():
        file.write(f'\n{key},{value}')
    file.close


def search_saved_data(filepath, column_name, search_value):
    df = pd.read_csv(filepath)

    # search for the value in the searched columm
    index = df[df[column_name] == search_value].index[0]

    # access the data from the next columm
    next_column_value = df.iloc[index, df.columns.get_loc(column_name) + 1]

    #returns the data from the next columm
    return next_column_value

def if_in_csv(filepath,columm_name,search_value):
    search_for=search_saved_data(filepath,columm_name,search_value)
    if search_for  !=None:
        return True
    else:
        return False


def replace_in_csv(filepath, columm_name, search_value, replace_data):
    # CSV-Datei einlesen
    df = pd.read_csv(filepath)

    #search for the value of the choosen columm
    df.loc[df[columm_name] == search_value, columm_name] = replace_data

    # saves the changed csv file
    df.to_csv(filepath, index=False)

def add_data_with_checks(filepath,file_name,columm_name,data_to_add):
    new_filepath=filesystem(filepath)
    fullpath=new_filepath+file_name
    if check_if_exist(fullpath)==True:
        searched_data=search_saved_data(fullpath,columm_name,data_to_add)
        if searched_data==data_to_add:
            replace_in_csv(fullpath,columm_name)
    else:
        csv_file_frame_create(fullpath,["data_from","data"])
        csv_file_add_data(fullpath,data_to_add)

def convert_to_dictionary(key,value):
    dictionary={}
    dictionary.update({key:value})
    return dictionary    