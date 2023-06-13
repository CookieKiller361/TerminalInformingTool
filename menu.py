import os

#clears the terminal
def clear_Terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

#menu function is the structure for menus
def menu(menu_title,*option_points):
    clear_Terminal()
    print(f'{menu_title}')
    index_number=0
    for options in option_points:
        index_number+=1
        print(f'{index_number}. {options}')
    choosen=input('Choose a Number: ')
    return int(choosen)

#the menu function need a error protection for number out of index 