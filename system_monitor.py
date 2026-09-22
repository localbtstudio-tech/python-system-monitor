import logging
import platform
import time

import psutil


logger = logging.getLogger(__name__)


class SystemMonitor:

    def __init__(self, config):
        self.config = config
        self.app_name = config["app_name"]
        self.version = config["version"]
        self.cpu_delay = config["cpu_delay"]
        self.process_limit = config["process_limit"]

        logger.info("SystemMonitor initialized")

    def cpu_usage(self):
        logger.info("Checking CPU usage")

        print("\nMeasuring CPU...")

        time.sleep(self.cpu_delay)

        cpu = psutil.cpu_percent()

        print("CPU Usage:", cpu, "%")

        logger.info("CPU usage: %.2f%%", cpu)

    def ram_usage(self):
        logger.info("Checking RAM usage")

        memory = psutil.virtual_memory()

        print("\nRAM Usage:", memory.percent, "%")

        logger.info("RAM usage: %.2f%%", memory.percent)

    def disk_usage(self):
        logger.info("Checking disk usage")

        disk = psutil.disk_usage("/")

        print("\nDisk Usage:", disk.percent, "%")

        logger.info("Disk usage: %.2f%%", disk.percent)

    def system_information(self):
        logger.info("Checking system information")

        print("\n--- System Information ---")

        print("OS:", platform.system())
        print("OS Version:", platform.version())
        print("Architecture:", platform.machine())
        print("CPU Cores:", psutil.cpu_count())
        print("Hostname:", platform.node())

    def network_information(self):
        logger.info("Checking network information")

        print("\n--- Network Information ---")

        interfaces = psutil.net_if_addrs()

        print("\nNetwork Interfaces:")

        for interface in interfaces:
            print("-", interface)

        stats = psutil.net_io_counters()

        print("\nNetwork Statistics:")
        print("Bytes Sent:", stats.bytes_sent)
        print("Bytes Received:", stats.bytes_recv)

    def process_information(self):
        logger.info("Checking running processes")

        print("\n--- Running Processes ---")

        print("PID\tName\t\tCPU%\tMemory%")

        count = 0

        for process in psutil.process_iter(
            ["pid", "name", "cpu_percent", "memory_percent"]
        ):
            if count >= self.process_limit:
                break

            try:
                info = process.info

                print(
                    info["pid"],
                    info["name"],
                    info["cpu_percent"],
                    info["memory_percent"]
                )

                count += 1

            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

        logger.info(
            "Displayed %d running processes",
            count
        )

    def full_system_status(self):
        logger.info("Checking full system status")

        print("\n--- System Status ---")

        print("\nCPU:")
        self.cpu_usage()

        print("\nRAM:")
        self.ram_usage()

        print("\nDisk:")
        self.disk_usage()

        print("\nSystem:")
        self.system_information()

        print("\nNetwork:")
        self.network_information()

        print("\nProcesses:")
        self.process_information()