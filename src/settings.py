import os
import signal
import sys
import time
import json
from copy import copy

data_path = "extras/data.json"

class FanSettings:
   
    def __init__(self):
        self.__data = dict()

    @staticmethod
    def load(path: str = data_path):
        fan_info = FanSettings()
        with open(path, "r") as data_file:
            data = json.load(data_file)

        defaults: dict = data["defaults"]
         
        fan_info.__data = {
            "defaults" : defaults,
            "current" : copy(defaults)
        }
        fan_info.save()
        return fan_info
    
    def save(self):
        data = json.load(data_path)
        data["defaults"] = self.__data["defaults"]
        with open(data_path, "r") as data_file:
            json.dump(data, data_file, indent=4)
   

 