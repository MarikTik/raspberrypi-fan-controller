import argparse

class CLI:
    def __init__(self):
        parser = argparse.ArgumentParser(description='Control a Raspberry Pi fan.')
        parser.add_argument('--mode', type=str, choices=['ON', 'OFF', 'AUTO'], required=True, help='Fan mode')
        parser.add_argument('--pin', type=int, default=23, help='GPIO pin connected to the fan')
        parser.add_argument('--critical_temperature', type=float, default=50.0, help='Temperature to turn the fan on')
        parser.add_argument('--minimum_temperature', type=float, default=30.0, help='Temperature to turn the fan off')

        self.args = parser.parse_args()

    def get_args(self):
        return self.args
