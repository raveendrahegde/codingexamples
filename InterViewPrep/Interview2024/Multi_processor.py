import threading
from queue import Queue
import time

class Processor(threading.Thread):
  def __init__(self, my_q, lock) -> None:
    super().__init__()
    self.my_q = my_q
    self.stopped = False
    self.lock = lock
  
  def strProcessor(self, str):
    print(f"----{str}----")
    return
  
  def run(self):
    while not self.stopped:
      with self.lock:
        if self.my_q.qsize() != 0:
          item = self.my_q.get()
          self.strProcessor(item)
  
  def stop(self):
    print("Stopping")
    self.stopped = True


class Manager():
  def __init__(self, items, concurrent) -> None:
    self.items = items
    self.concurrent = concurrent
    self.threads = []
    self.in_q = Queue()
    self.lock = threading.Lock()

  def process(self):
    for i in range(self.concurrent):
      thread = Processor(self.in_q, self.lock)
      self.threads.append(thread)
      thread.start()

    with self.lock: # Using `with`` so that we dont have to use acquire() and release()
      for item in self.items:
        self.in_q.put(item)
    
    while self.in_q.qsize() != 0:
      print(f"Processing {self.in_q.qsize()} items")
      time.sleep(5)

    for thread in self.threads:
      thread.stop()
    
    for thread in self.threads:
      thread.join()

if __name__ == "__main__":
  sentense = input("Enter a sentence:")
  words = sentense.split()

  mgr = Manager(words, 3)
  mgr.process()