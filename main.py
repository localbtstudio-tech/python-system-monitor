import json
import logging

from system_monitor import SystemMonitor


def load_config():
    try:
        with open("config.json", "r", encoding="utf-8") as file:
            config = json.load(file)

        return config

    except FileNotFoundError:
        print("Configuration file not found.")
        return None

    except json.JSONDecodeError:
        print("Invalid JSON configuration.")
        return None


def setup_logging(log_file):
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )


def display_menu(config):
    print("-------------------------------------")
    print(f"|        {config['app_name']}      |")
    print(f"|               {config['version']}                |")
    print("-------------------------------------")

    print("1. CPU Usage")
    print("2. RAM Usage")
    print("3. Disk Usage")
    print("4. Full System Status")
    print("5. System Information")
    print("6. Network Information")
    print("7. Running Processes")
    print("8. Exit")


def main():
    config = load_config()

    if config is None:
        return

    setup_logging(config["log_file"])

    logging.info("Application started")

    monitor = SystemMonitor(config)

    while True:
        display_menu(config)

        try:
            option = int(input("Choose an option: "))

            if option == 1:
                monitor.cpu_usage()

            elif option == 2:
                monitor.ram_usage()

            elif option == 3:
                monitor.disk_usage()

            elif option == 4:
                monitor.full_system_status()

            elif option == 5:
                monitor.system_information()

            elif option == 6:
                monitor.network_information()

            elif option == 7:
                monitor.process_information()

            elif option == 8:
                print("Goodbye!")

                logging.info("Application closed")

                break

            else:
                print("Invalid option.")

        except ValueError:
            print("Please enter a number.")
            logging.warning("Invalid menu input")


if __name__ == "__main__":
    main()