import psutil
import time
import platform


def display_menu():
    print("-------------------------------------")
    print("|        PYTHON SYSTEM MONITOR      |")
    print("|               V1.1                |")
    print("-------------------------------------")

    print("1. CPU Usage")
    print("2. RAM Usage")
    print("3. Disk Usage")
    print("4. Full System Status")
    print("5. System Information")
    print("6. Exit")


def cpu_usage():
    print("\nMeasuring CPU...")

    time.sleep(1)

    cpu = psutil.cpu_percent()

    print("CPU Usage:", cpu, "%")


def ram_usage():
    memory = psutil.virtual_memory()

    print("\nRAM Usage:", memory.percent, "%")


def disk_usage():
    disk = psutil.disk_usage("/")

    print("\nDisk Usage:", disk.percent, "%")


def system_information():
    print("\n--- System Information ---")

    print("OS:", platform.system())
    print("OS Version:", platform.version())
    print("Architecture:", platform.machine())
    print("CPU Cores:", psutil.cpu_count())
    print("Hostname:", platform.node())


def full_system_status():
    print("\n--- System Status ---")

    print("\nCPU:")
    cpu_usage()

    print("\nRAM:")
    ram_usage()

    print("\nDisk:")
    disk_usage()

    print("\nSystem:")
    system_information()


def main():
    while True:
        display_menu()

        try:
            option = int(input("Choose an option: "))

            if option == 1:
                cpu_usage()

            elif option == 2:
                ram_usage()

            elif option == 3:
                disk_usage()

            elif option == 4:
                full_system_status()

            elif option == 5:
                system_information()

            elif option == 6:
                print("Goodbye!")
                break

            else:
                print("Invalid option.")

        except ValueError:
            print("Please enter a number.")


if __name__ == "__main__":
    main()