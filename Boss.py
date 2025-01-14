import queue_mc as q_mc
from task import Task
import time


qclient = q_mc.QueueClient()
task_id = 1  
task_result = Task()

while True:
    new_task = Task(task_id, 1000) 
    qclient.taskQueue.put(new_task)
    print(f"Tâche ajoutée:  {new_task.identifier}")
    task_id += 1
    try:
        while not qclient.resultQueue.empty():
            task_result = qclient.resultQueue.get()
            print(f"Tache récupéré : {task_result.identifier} en  {task_result.time} s")
    except Exception as e:
        print(f"Erreur inattendue : {e}")
    time.sleep(2)
