#function create name and list()
def createList():
    while True:
        ans = input("Press y for yes, n for no if you want to create a List: ")
        if  ans == "y":
            list_name = input("input list name: ")
            user_list=[]
            return list_name, user_list

        elif ans == "n":
            return None
            #functionaddToDo
           
        else:
            print("invalid")

#function take in to do 
def addTodo(created_list):
    toDo = input("What ToDo: ")
    # add section that conctenates the item number out for the user 

    created_list.append(toDo)
    return created_list

#function delete to do
def deleteTodo(created_list):
    list_index = int(input("what number would you like to delete: "))
    if list_index < len(created_list): 
        confirm = input("click y to confirm or n to reject: ")
        if confirm == "y":
            print ("{} has been removed".format((created_list[list_index-1])))
            created_list.remove(created_list[list_index-1])
            return created_list
        else:
            return None
    else : 
        print("that number does not exist")


def main():
    
    list_name, created_list = createList()
    print("{} \n {}".format(list_name, created_list))

    while True:  
        query_check = input("type a to add, d to delete: ")  
        if query_check == "a":
            addTodo(created_list)
        elif query_check == "d":
            deleteTodo(created_list)
        print("{} \n {}".format(list_name, created_list))
        

main()
