from multiprocessing.managers import BaseManager
from multiprocessing import Queue


class QueueClient:
    def __init__(self):
        QueueManager.register("get_taskQueue")
        QueueManager.register("get_resultQueue")
        m = QueueManager(address=("", 2007), authkey=b"Hello")
        m.connect()
        self.taskQueue = m.get_taskQueue()
        self.resultQueue = m.get_resultQueue()

class QueueManager(BaseManager):
    pass

if __name__ == "__main__":
    taskQueue = Queue()
    resultQueue = Queue()
    QueueManager.register("get_taskQueue", callable=lambda: taskQueue)
    QueueManager.register("get_resultQueue", callable=lambda: resultQueue)
    manager = QueueManager(address=("", 2007), authkey=b"Hello")
    serveur = manager.get_server()
    serveur.serve_forever()
