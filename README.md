# PYTHON SYSTEM MONITOR 🖥️

<div align="center">

### A lightweight command-line system monitoring tool built with Python.

**Python · psutil · platform · Functions · Control Flow · CLI**

<br>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![psutil](https://img.shields.io/badge/Library-psutil-black?style=for-the-badge)
![platform](https://img.shields.io/badge/Library-platform-black?style=for-the-badge)
![CLI](https://img.shields.io/badge/Interface-CLI-black?style=for-the-badge)
![Version](https://img.shields.io/badge/Version-1.2-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-In%20Development-orange?style=for-the-badge)

</div>

---

## ◼︎ The Project

**Python System Monitor** is a command-line system monitoring tool built with Python, `psutil`, and `platform`.

The project is being developed step by step, starting with basic system resource monitoring and gradually expanding toward a more structured monitoring application.

The current version focuses on:

* CPU usage
* RAM usage
* Disk usage
* System information
* Network information
* Full system status
* Interactive CLI menu

> **Start simple. Build progressively.**

---

## ✦ V1.2 — Network Information

The current version extends the original monitor with **system information** and **network monitoring**.

```text
┌─────────────────────────────────────┐
│       PYTHON SYSTEM MONITOR         │
│               V1.2                  │
├─────────────────────────────────────┤
│  1. CPU Usage                       │
│  2. RAM Usage                       │
│  3. Disk Usage                      │
│  4. Full System Status              │
│  5. System Information              │
│  6. Network Information             │
│  7. Exit                            │
└─────────────────────────────────────┘
```

### Current Features

* 🧠 CPU Usage
* 💾 RAM Usage
* 💿 Disk Usage
* 🖥️ Operating System Information
* ⚙️ OS Version
* 🔧 System Architecture
* 🔢 CPU Core Count
* 🏷️ Hostname
* 🌐 Network Interfaces
* 📤 Bytes Sent
* 📥 Bytes Received
* 📊 Full System Status
* 🔄 Continuous CLI loop
* ❌ Invalid option handling
* ⚠️ Input error handling
* 👋 Clean exit

---

## ⚙️ How It Works

The program uses `psutil` and `platform` to retrieve information directly from the operating system.

```text
USER
 │
 ▼
Display Menu
 │
 ▼
Select Option
 │
 ├────────────┬────────────┬──────────────┬──────────────┐
 ▼            ▼            ▼              ▼              ▼
CPU          RAM          Disk          System        Network
 │            │            │              │              │
 ▼            ▼            ▼              ▼              ▼
psutil       psutil       psutil       platform       psutil
 │            │            │              │              │
 └────────────┴────────────┴──────────────┴──────────────┘
                              │
                              ▼
                           RESULT
```

The program keeps running inside a `while` loop until the user selects **Exit**.

---

## 🧠 Concepts Practiced

| Concept        | Used For                               |
| -------------- | -------------------------------------- |
| `import`       | Loading Python libraries               |
| `psutil`       | Reading system and network information |
| `platform`     | Reading operating system information   |
| `def`          | Creating reusable functions            |
| `while`        | Keeping the monitor running            |
| `if / elif`    | Handling menu options                  |
| `input()`      | Receiving user input                   |
| `int()`        | Converting menu input                  |
| `try / except` | Handling invalid input                 |
| `for`          | Iterating through network interfaces   |
| `break`        | Exiting the program                    |
| `time.sleep()` | Adding a measurement delay             |
| `if __name__`  | Running the main program               |

---

## 🔧 Main Functions

The current version is divided into simple functions:

```text
main()
 │
 ├── display_menu()
 │
 ├── cpu_usage()
 │
 ├── ram_usage()
 │
 ├── disk_usage()
 │
 ├── system_information()
 │
 ├── network_information()
 │
 └── full_system_status()
```

### `cpu_usage()`

Uses:

```python
psutil.cpu_percent()
```

to measure the current CPU utilization.

---

### `ram_usage()`

Uses:

```python
psutil.virtual_memory()
```

to retrieve RAM information and display the percentage currently in use.

---

### `disk_usage()`

Uses:

```python
psutil.disk_usage("/")
```

to retrieve disk usage information.

---

### `system_information()`

Uses the `platform` module and `psutil` to display basic system information.

```python
platform.system()
platform.version()
platform.machine()
platform.node()
psutil.cpu_count()
```

The function displays:

```text
OS
OS Version
Architecture
CPU Cores
Hostname
```

---

### `network_information()`

Uses:

```python
psutil.net_if_addrs()
```

to detect available network interfaces.

It also uses:

```python
psutil.net_io_counters()
```

to retrieve network traffic statistics.

The current version displays:

```text
Network Interfaces
Bytes Sent
Bytes Received
```

---

### `full_system_status()`

Combines the monitoring functions into one system overview:

```text
CPU
RAM
Disk
System
Network
```

This provides a quick snapshot of the current machine.

---

## 📈 Development Roadmap

The project will gradually evolve from a basic monitor into a more complete system monitoring application.

### V1.0 — Basic Monitor

```text
├── Menu
├── CPU Usage
├── RAM Usage
├── Disk Usage
└── Full System Status
```

**Status:** ✅ Complete

---

### V1.1 — System Information

```text
├── OS
├── OS Version
├── Architecture
├── CPU Cores
└── Hostname
```

**Status:** ✅ Complete

---

### V1.2 — Network Information

```text
├── Network Interfaces
├── Bytes Sent
├── Bytes Received
└── Network Statistics
```

**Status:** ✅ Complete

---

### V1.3 — Process Monitoring

The next version will introduce process monitoring.

```text
├── Running Processes
├── PID
├── Process Name
├── CPU Usage
└── Memory Usage
```

**Status:** ⬜ Planned

---

### V2.0 — Professional Version

The project will then move toward a more structured architecture.

```text
├── OOP
├── Modules
├── Classes
├── Logging
├── JSON
└── Configuration
```

**Status:** ⬜ Future

---

## 🛠️ Technologies

### Language

**Python 3**

### Libraries

**psutil**

Used to access system resources and network information.

**platform**

Used to retrieve operating system and machine information.

### Interface

**Command Line Interface (CLI)**

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/localbtstudio-tech/python-system-monitor.git
```

### 2. Enter the project

```bash
cd python-system-monitor
```

### 3. Install the dependency

```bash
pip install psutil
```

### 4. Run the program

```bash
python main.py
```

---

## 🎮 Example

```text
-------------------------------------
|        PYTHON SYSTEM MONITOR      |
|               V1.2                |
-------------------------------------

1. CPU Usage
2. RAM Usage
3. Disk Usage
4. Full System Status
5. System Information
6. Network Information
7. Exit

Choose an option: 4

--- System Status ---

CPU:

Measuring CPU...
CPU Usage: 12.5 %

RAM:

RAM Usage: 48.7 %

Disk:

Disk Usage: 61.2 %

System:

--- System Information ---
OS: Windows
OS Version: ...
Architecture: AMD64
CPU Cores: 12
Hostname: DESKTOP-...

Network:

--- Network Information ---

Network Interfaces:
- WiFi
- Local Area Connection* 1
- Local Area Connection* 2

Network Statistics:
Bytes Sent: ...
Bytes Received: ...
```

---

## 📁 Project Structure

```text
python-system-monitor/
│
├── main.py
├── README.md
└── .gitignore
```

The project currently uses a single Python file to keep the architecture simple.

As new versions are introduced, the project will gradually become more modular.

---

## ◼︎ Why I Built This

This project is part of my **Python learning and cybersecurity development journey**.

The goal is to start with simple system monitoring and progressively introduce more advanced Python concepts.

```text
Python Fundamentals
        │
        ▼
System Monitoring
        │
        ▼
System Information
        │
        ▼
Network Monitoring
        │
        ▼
Process Monitoring
        │
        ▼
Modules & OOP
        │
        ▼
Structured Application
```

The project is designed to grow alongside my Python skills.

> **Learn → Build → Improve → Refactor**

---

## 🔮 Future Direction

After the core CLI version is completed, possible improvements include:

* [ ] Display IP addresses
* [ ] Add detailed network information
* [ ] Add process monitoring
* [ ] Display process CPU usage
* [ ] Display process memory usage
* [ ] Add logging system
* [ ] Add JSON configuration
* [ ] Refactor into OOP
* [ ] Split the application into modules
* [ ] Add configuration management
* [ ] Improve error handling
* [ ] Build a GUI version
* [ ] Build a system monitoring dashboard

---

## 👨‍💻 Author

**Hamza Weslati**

IT Student · Web Developer · Software Development

<br>

[![GitHub](https://img.shields.io/badge/GitHub-localbtstudio--tech-181717?style=for-the-badge\&logo=github)](https://github.com/localbtstudio-tech)

[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-ff003c?style=for-the-badge)](https://localbtstudio-tech.github.io/Portfolio/)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Hamza_Weslati-0A66C2?style=for-the-badge\&logo=linkedin)](https://www.linkedin.com/in/hamza-weslati-9a99a8419/)

---

<div align="center">

### 🖥️ PYTHON SYSTEM MONITOR

*Built step by step with Python.*

**© 2026 Hamza Weslati**

</div>
