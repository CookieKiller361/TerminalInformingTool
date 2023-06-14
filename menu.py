import os

#clears the terminal
def clear_Terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

#menu function is the structure for menus
def menu(menu_title,*option_points):
    clear_Terminal()
    print(f'{menu_title}')
    index_number=0
    index_list=[]
    
    for options in option_points:
        index_number+=1
        index_list.append(index_number)
        print(f'{index_number}. {options}')
    while True:
        index_list.sort()
        choosen=input('Choose a Number: ')
        choosen=int(choosen)
        if choosen in index_list:
            return choosen
        
        else:
            print("Number not available, please try a number from the menu!")