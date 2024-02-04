from cli import CLI
from fan import Fan
import warnings
 
warnings.filterwarnings("ignore", message="Falling back from")


def main():
    cli = CLI()
    args = cli.get_args()

    fan = Fan(pin=args.pin)
    fan.mode(args.mode)
    
    print(f"Fan set to {args.mode} mode.")
    fan.spin(critical_temperature=args.critical_temperature, minimum_temperature=args.minimum_temperature)

if __name__ == "__main__":
     main()