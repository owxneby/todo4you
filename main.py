#function create name and list()
def createList():
    while True:
        ans = input("Press y for yes, n for no if you want to create a List: ")
        if  ans.lower() == "y":
            list_name = input("input list name: ")
            user_list=[]
            return list_name, user_list

        elif ans.lower() == "n":
            return None
            #functionaddToDo
           
        else:
            print("invalid")

#function take in to do 
def addTodo(created_list):
    toDo = input("What ToDo: ")
    created_list.append(toDo)
    return created_list

#function delete to do
def deleteTodo(created_list):
    list_index = int(input("what number would you like to delete: "))
    if list_index < len(created_list): 
        confirm = input("click y to confirm or n to reject: ")
        if confirm.lower() == "y":
            print ("{} has been removed".format((created_list[list_index-1])))
            created_list.remove(created_list[list_index-1])
            return created_list
        else:
            print ("Deletion cancelled")
    else : 
        print("that number does not exist")

#function displaylist
def displayList(list_name, created_list):
    print("{}".format(list_name))
    for item_index, item in enumerate(created_list, start=1):
        print("{}. {}".format(item_index, item))

def main():
    
    list_name, created_list = createList()
    if list_name is None:  # Handle case where no list is created
        print("No list created. Exiting.")
        return

    while True:  
        displayList(list_name, created_list)
        query_check = input("type a to add, d to delete or q to quit: ")  
        if query_check.lower() == "a":
            addTodo(created_list)
        elif query_check.lower() == "d":
            deleteTodo(created_list)
        elif query_check.lower() == "q":
            print("Exit program")
            break
        else:
            print("Invalid option")
        
main() 
