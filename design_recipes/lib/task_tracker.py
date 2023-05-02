class TaskTracker():
    def __init__(self):
        self.task_list = []

    def add_task(self, task):
        self.task_list.append(task)

    def incomplete(self):
        return self.task_list
    
    def complete(self, index):
        if index < 0 or index >=len(self.task_list):
            raise Exception("There is no task")
        del self.task_list[index]

        



