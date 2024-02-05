import argparse

class CLI:
    def __init__(self):
        parser = argparse.ArgumentParser(description='Control a Raspberry Pi fan.')
        subparsers = parser.add_subparsers(dest='command')
        
        # Subparser for setting mode
        parser_set = subparsers.add_parser('set', help='Set fan mode and options')
        parser_set.add_argument('--mode', type=str, choices=['ON', 'OFF', 'AUTO', 'on', 'off', 'auto'], help='Fan mode')
        parser_set.add_argument('--pin', type=int, default=23, help='GPIO pin connected to the fan')
        parser_set.add_argument('--critical_temperature', type=float, default=60.0, help='Temperature to turn the fan on')
        parser_set.add_argument('--minimal_temperature', type=float, default=40.0, help='Temperature to turn the fan off')

        # Subparser for info
        parser_info = subparsers.add_parser('info', help='Display fan configuration and status')

        self._args = parser.parse_args()

    def get_args(self):
        return self._args
