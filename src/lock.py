import os
import signal
import sys
import json
from typing import Callable

class Lock:

     @staticmethod 
     def release(signum, frame):
          for method in Lock.__release_methods:
              method()

          with open(Lock.__process_data_path, "w") as process_data_file: # in case last instance was closed.
              json.dumps(process_data_file, {"pid" : 0}, indent=4)

          sys.exit(0) 

     @staticmethod
     def acquire():
          with open(Lock.__process_data_path, "rw") as process_data_file:
             data: dict = json.load(process_data_file)
             pid = data.get("pid", 0)
             if pid:
                  try:  
                    os.kill(pid, signal.SIGTERM)
                  except ProcessLookupError:
                    pass
                  
             data["pid"] = os.getpid()
             json.dump(process_data_file, data, indent=4)

     @staticmethod
     def on_release(*methods: Callable):
         Lock.__release_methods = methods

     __release_methods = ()
     __process_data_path = "extras/settings.json"

signal.signal(signal.SIGTERM, Lock.release)
 
 
 