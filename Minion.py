import queue_mc as q_mc
from task import Task

queueClient = q_mc.QueueClient()
result = Task()

while True:
    task = queueClient.taskQueue.get()
    task.work()
    print("tache : " + str(task.identifier) + " exécutée en : " + str(task.time))
    queueClient.resultQueue.put(task)
