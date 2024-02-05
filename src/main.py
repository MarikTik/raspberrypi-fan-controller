from cli import CLI
from fan import Fan
import warnings

warnings.filterwarnings("ignore", message="Falling back from")

def main():
    cli = CLI()
    args = cli.get_args()
    fan = Fan()
    if args.command == 'set':
        fan.set_pin(args.pin)
        fan.set_mode(args.mode)
        
        print(f"Fan set to {args.mode} mode.")
        # Assuming you only want to start spinning the fan if mode is explicitly set
        if args.mode:
            fan.spin(critical_temperature=args.critical_temperature, minimal_temperature=args.minimal_temperature)
    elif args.command == 'info':
        print(fan)

if __name__ == "__main__":
    main()
