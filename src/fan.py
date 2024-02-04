from gpiozero import OutputDevice
from typing import Literal
import time

# Set up the GPIO pin (BCM numbering) for the fan
FAN_PIN = 23

 
class Fan:
    def __init__(self, pin:int = FAN_PIN) -> None:
        self._fan = OutputDevice(pin=pin)
        self._mode = "AUTO"

    def mode(self, mode: Literal["ON", "OFF", "AUTO"]):
        if isinstance(mode, str):
            self._mode = mode.upper()
        else:
            print(f"Wrong argument type {mode}. Expected 'str', got '{type(mode)}'")

        if mode in ("ON", "OFF", "AUTO"):
            self._mode = mode 


    def __get_cpu_temperature():    
     """Read the CPU temperature from the system."""
     temperature_read = "/sys/class/thermal/thermal_zone0/temp"
     with open(temperature_read, "r") as file:
          cpu_temp = int(file.read()) / 1000.0
     return cpu_temp


# def control_fan_based_on_temperature(critical_temp=60.0, sleep_time=5):
#     while True:
#         cpu_temp = get_cpu_temperature()
#         print(f"CPU Temperature: {cpu_temp}°C")
        
#         if cpu_temp > critical_temp:
#             if not fan.is_active:
#                 fan.on()
#                 print("Fan turned ON due to high temperature.")
#         else:
#             if fan.is_active:
#                 fan.off()
#                 print("Fan turned OFF as temperature is normal.")
                
#         time.sleep(sleep_time)

 