import psutil
import time


def display_menu():
    print("-------------------------------------")
    print("|        PYTHON SYSTEM MONITOR      |")
    print("|               V1.0                |")
    print("-------------------------------------")

    print("1. CPU Usage")
    print("2. RAM Usage")
    print("3. Disk Usage")
    print("4. Full System Status")
    print("5. Exit")


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


def full_system_status():
    print("\n--- System Status ---")

    print("\nCPU:")
    cpu_usage()

    print("\nRAM:")
    ram_usage()

    print("\nDisk:")
    disk_usage()


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
                print("Goodbye!")
                break

            else:
                print("Invalid option.")

        except ValueError:
            print("Please enter a number.")


if __name__ == "__main__":
    main()