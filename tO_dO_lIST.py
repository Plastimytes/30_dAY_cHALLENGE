####This is a today project for theb github 30 day challenge###
###create class

class ToDoList:
    def _init_(self):
     self.tasks=[]
    def add_task(self, task):
     self.tasks.append({"task":task, "completed": False})
     print(f'Task "{task}"" created')

    def view_tasks(self):
        if not self.tasks:
            print("No tasks")
            return
        print("Give tasks")
        for idx, task in enumerate(self.tasks,start=1):
            print(f"{idx}.{task}")

    def delete_tasks(self,index):
        try:
            removed_task = self.tasks.pop(index-1)
            print(f"Task {removed_task} removed")    
        except IndexError:
            print("Invalid task number")

    def run(self):
        while True:
            print("\n To_Do LIst Menu")   
            print("1. Add Task")     
            print("2. View Tasks")
            print("3.Delete Task")
            print("4. Exit ") 
            choices=input("Choose an Option (1-4)")  

            if choices =="1":
                task =input("Enter a Task")
                self.add_task(task)
            elif choices =="2":
                self.view_tasks()
            elif choices =="3":
                self.view_tasks()
                try:
                    task_num=int(input("Enter a Task to delete"))
                    self.delete_task(task_num)
                except ValueError:
                    print("Please enter a valid number")
            elif choices =="4":
                print("Exiting the app")
            else:
                print("Invalid choice. Please try again")
    if __name__=="_main_":
     ToDo_list = ToDoList()
     ToDo_list.run()       


     ###The python code is being stupid anyone who would give any insights is welcome         







