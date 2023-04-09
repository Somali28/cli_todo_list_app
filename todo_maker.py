import numpy as np

def input_from_console():
    inp = input('Enter number ')
    return inp

def print_all_options(todo_list):
    print("-1 : Exit TodoManager")
    print(" 0 : Help")
    print(" 1 : Display all Tasks")
    print(" 2 : Add a Task")
    print(" 3 : Remove a Task")

def parse_command(todo_list, num):
    switcher = {
        0: print_all_options,
        1: print_todo_list,
        2: add_item,
        3: delete_item
    }
    return switcher[num](todo_list)
    

def print_todo_list(todo_list):
    if len(todo_list) == 0:
        print("No Task to display!")
    for i in range(len(todo_list)):
        print(i+1, end=" ")
        print(todo_list[i])

def add_item(todo_list):
    item = input('Enter task for adding in ToDo List :')
    todo_list.append(item)

def delete_item(todo_list):
    num = input('Enter the serial num of Task to be removed :')
    todo_list.pop(int(num)-1)


def main():

    print("Welcome to ToDo List")
    todolst = []
    print_all_options(todolst)
    while True:
        num = int(input_from_console())
        if num == -1:
            break
        parse_command(todolst, num)

    

if __name__ == "__main__":
    main()