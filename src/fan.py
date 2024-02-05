from gpiozero import OutputDevice
from typing import Literal
import time

# Set up the GPIO pin (BCM numbering) for the fan
FAN_PIN = 23


class Fan:
    def __init__(self, pin: int = FAN_PIN) -> None:
        self._pin = pin
        self._mode = "AUTO"
        self._critical_temperature = 60
        self._minimal_temperature = 35
        self.__update()

    def __update(self):
        self._fan = OutputDevice(self._pin)

    def set_pin(self, pin: int):
        self._pin = pin

    def __str__(self) -> str:
        message = f"pin: GPIO {self._pin}\nmode: {self._mode}\n"
        if self._mode == "AUTO":
            message += f"critical_temperature: {self._critical_temperature} °C\nminimal_temperature: {self._minimal_temperature} °C"

        return message
        


    def set_mode(self, mode: Literal["ON", "OFF", "AUTO"]):
        mode_u = mode.upper()
        if mode_u in ("ON", "OFF", "AUTO"):
            self._mode = mode_u
        else:
            print(f"Invalid mode: {mode}. Expected 'ON', 'OFF', or 'AUTO'.")


    def spin(self, critical_temperature: float, minimal_temperature: float):
        self._critical_temperature = critical_temperature
        self._minimal_temperature = minimal_temperature

        while True:
            match self._mode:
                case "OFF":
                    self._fan.off()

                case "ON":
                    self._fan.on()

                case "AUTO":
                    temperature = Fan.get_cpu_temperature()
                    self._fan.off()
                    if temperature >= critical_temperature:
                        self._fan.on()
                    elif temperature <= minimal_temperature:
                        self._fan.off()
                    time.sleep(30)  # Check every 30 seconds

    @staticmethod
    def get_cpu_temperature():
        """Read the CPU temperature from the system."""
        temperature_read = "/sys/class/thermal/thermal_zone0/temp"
        with open(temperature_read, "r") as file:
            cpu_temp = int(file.read()) / 1000.0
        return cpu_temp
