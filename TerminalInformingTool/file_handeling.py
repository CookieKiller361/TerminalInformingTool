import os
import pandas as pd


def check_if_exist(filepath):
    if os.path.exists(filepath):
        return True
    else:
        return False


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


def replace_in_csv(filepath, column_name, search_value, replace_data):
    # CSV-Datei einlesen
    df = pd.read_csv(filepath)

    #search for the value of the choosen columm
    df.loc[df[column_name] == search_value, column_name] = replace_data

    # saves the changed csv file
    df.to_csv(filepath, index=False)