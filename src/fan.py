from gpiozero import OutputDevice
from typing import Literal
import time

# Set up the GPIO pin (BCM numbering) for the fan
FAN_PIN = 23

class Fan:
    def __init__(self, pin: int = FAN_PIN) -> None:
        self._fan = OutputDevice(pin=pin)
        self._mode = "AUTO"
    
    @staticmethod
    def get_cpu_temperature():
        """Read the CPU temperature from the system."""
        temperature_read = "/sys/class/thermal/thermal_zone0/temp"
        with open(temperature_read, "r") as file:
            cpu_temp = int(file.read()) / 1000.0
        return cpu_temp

    def mode(self, mode: Literal["ON", "OFF", "AUTO"]):
        mode_u = mode.upper()
        if mode_u in ("ON", "OFF", "AUTO"):
            self._mode = mode_u
        else:
            print(f"Invalid mode: {mode}. Expected 'ON', 'OFF', or 'AUTO'.")

    def spin(self, critical_temperature: float = 55.0, minimum_temperature: float = 30.0):
        while True:
            temperature = Fan.get_cpu_temperature()
            match self._mode:
                case "OFF":
                    self._fan.off()
                case "ON":
                    self._fan.on()
                case "AUTO":
                    if temperature >= critical_temperature:
                        self._fan.on()
                    elif temperature <= minimum_temperature:
                        self._fan.off()
            time.sleep(10)  # Check every 10 seconds