# PYTHON SYSTEM MONITOR 🖥️

<div align="center">

### A lightweight command-line system monitoring tool built with Python.

**Python · psutil · platform · Functions · Control Flow · CLI**

<br>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![psutil](https://img.shields.io/badge/Library-psutil-black?style=for-the-badge)
![platform](https://img.shields.io/badge/Library-platform-black?style=for-the-badge)
![CLI](https://img.shields.io/badge/Interface-CLI-black?style=for-the-badge)
![Version](https://img.shields.io/badge/Version-1.3-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-In%20Development-orange?style=for-the-badge)

</div>

---

## ◼︎ The Project

**Python System Monitor** is a command-line system monitoring tool built with Python, `psutil`, and `platform`.

The project is being developed step by step, starting with basic system resource monitoring and gradually expanding toward a more structured monitoring application.

The current version is **V1.3**.

The monitor currently provides:

* CPU usage
* RAM usage
* Disk usage
* System information
* Network information
* Running process information
* Full system status
* Interactive CLI menu

> **Start simple. Build progressively.**

---

## ✦ V1.3 — Process Monitoring

The current version introduces **process monitoring**, allowing the user to inspect running processes and their resource usage.

```text id="5p0t7x"
┌─────────────────────────────────────┐
│       PYTHON SYSTEM MONITOR         │
│               V1.3                  │
├─────────────────────────────────────┤
│  1. CPU Usage                       │
│  2. RAM Usage                       │
│  3. Disk Usage                      │
│  4. Full System Status              │
│  5. System Information              │
│  6. Network Information             │
│  7. Running Processes               │
│  8. Exit                            │
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
* ⚙️ Running Processes
* 🆔 Process IDs
* 📋 Process Names
* 🧠 Process CPU Usage
* 💾 Process Memory Usage
* 📊 Full System Status
* 🔄 Continuous CLI loop
* ❌ Invalid option handling
* ⚠️ Input error handling
* 🛡️ Process access error handling
* 👋 Clean exit

---

## ⚙️ How It Works

The program uses `psutil` and `platform` to retrieve information directly from the operating system.

```text id="c4f1rm"
                         PYTHON SYSTEM MONITOR
                                  │
                                  ▼
                              MAIN LOOP
                                  │
                                  ▼
                              MENU SYSTEM
                                  │
       ┌────────────┬────────────┬────────────┬────────────┬────────────┐
       ▼            ▼            ▼            ▼            ▼            ▼
      CPU          RAM          DISK        SYSTEM       NETWORK     PROCESSES
       │            │            │            │            │            │
       ▼            ▼            ▼            ▼            ▼            ▼
    psutil       psutil       psutil     platform      psutil       psutil
       │            │            │            │            │            │
       └────────────┴────────────┴────────────┴────────────┴────────────┘
                                      │
                                      ▼
                                   RESULT
```

The program keeps running inside a `while` loop until the user selects **Exit**.

---

## 🧩 System Monitoring

### CPU

The monitor uses:

```python
psutil.cpu_percent()
```

to measure the current CPU utilization.

A short delay is added before the measurement.

---

### RAM

The monitor uses:

```python
psutil.virtual_memory()
```

to retrieve memory statistics.

The current version displays the percentage of RAM being used.

---

### Disk

The monitor uses:

```python
psutil.disk_usage("/")
```

to retrieve disk usage information.

The current version displays the percentage of disk space being used.

---

## 🖥️ System Information

The system information module uses the `platform` module and `psutil`.

```text
┌──────────────────────────────┐
│      SYSTEM INFORMATION      │
├──────────────────────────────┤
│ OS                           │
│ OS Version                   │
│ Architecture                │
│ CPU Cores                    │
│ Hostname                     │
└──────────────────────────────┘
```

### Information Collected

* Operating System
* OS Version
* CPU Architecture
* CPU Core Count
* Hostname

The project uses:

```python
platform.system()
platform.version()
platform.machine()
platform.node()
psutil.cpu_count()
```

---

## 🌐 Network Information

The network module uses:

```python
psutil.net_if_addrs()
```

to detect available network interfaces.

It also uses:

```python
psutil.net_io_counters()
```

to retrieve network traffic statistics.

```text
┌─────────────────────────────────┐
│       NETWORK INFORMATION       │
├─────────────────────────────────┤
│ Network Interfaces              │
│                                 │
│ - WiFi                          │
│ - Ethernet                      │
│ - Other Interfaces              │
│                                 │
│ Network Statistics              │
│                                 │
│ Bytes Sent                      │
│ Bytes Received                  │
└─────────────────────────────────┘
```

### Current Network Data

* Network interface names
* Total bytes sent
* Total bytes received

---

## ⚙️ Process Monitoring

V1.3 introduces the ability to inspect currently running processes.

The project uses:

```python
psutil.process_iter(
    ["pid", "name", "cpu_percent", "memory_percent"]
)
```

to iterate through running processes.

```text
┌─────────────────────────────────────────┐
│           RUNNING PROCESSES             │
├──────────┬────────────────┬──────┬──────┤
│ PID      │ Name           │ CPU% │ RAM% │
├──────────┼────────────────┼──────┼──────┤
│ 1234     │ explorer.exe   │ 1.2  │ 0.8  │
│ 2456     │ python.exe     │ 0.4  │ 1.1  │
│ 3789     │ chrome.exe     │ 3.5  │ 4.2  │
└──────────┴────────────────┴──────┴──────┘
```

### Process Information

The monitor currently displays:

* PID
* Process Name
* CPU Usage
* Memory Usage

### Process Error Handling

Some processes may disappear while the program is reading them or may deny access.

The program handles:

```python
psutil.NoSuchProcess
psutil.AccessDenied
```

and skips those processes instead of terminating the entire application.

---

## 📊 Full System Status

The **Full System Status** option combines all monitoring modules into one overview.

```text
Full System Status
        │
        ├── CPU
        │
        ├── RAM
        │
        ├── Disk
        │
        ├── System Information
        │
        ├── Network Information
        │
        └── Running Processes
```

This allows the user to inspect the main system information from a single menu option.

---

## 🧠 Concepts Practiced

| Concept          | Used For                                         |
| ---------------- | ------------------------------------------------ |
| `import`         | Loading Python libraries                         |
| `psutil`         | Reading system, network, and process information |
| `platform`       | Reading operating system information             |
| `def`            | Creating reusable functions                      |
| `while`          | Keeping the monitor running                      |
| `if / elif`      | Handling menu options                            |
| `input()`        | Receiving user input                             |
| `int()`          | Converting menu input                            |
| `try / except`   | Handling invalid input                           |
| `for`            | Iterating through interfaces and processes       |
| `break`          | Exiting the program                              |
| `continue`       | Skipping inaccessible processes                  |
| `time.sleep()`   | Adding a measurement delay                       |
| `process_iter()` | Iterating through running processes              |
| `if __name__`    | Running the main program                         |

---

## 🔧 Main Functions

The current version is divided into simple functions:

```text id="r3tq9p"
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
 ├── process_information()
 │
 └── full_system_status()
```

### `cpu_usage()`

Measures the current CPU utilization using `psutil`.

```python
psutil.cpu_percent()
```

---

### `ram_usage()`

Retrieves the current memory usage.

```python
psutil.virtual_memory()
```

---

### `disk_usage()`

Retrieves disk usage information.

```python
psutil.disk_usage("/")
```

---

### `system_information()`

Retrieves operating system and machine information using `platform` and `psutil`.

---

### `network_information()`

Retrieves network interfaces and network traffic statistics.

---

### `process_information()`

Iterates through running processes and retrieves:

```text
PID
Name
CPU%
Memory%
```

It also handles processes that cannot be accessed.

---

### `full_system_status()`

Combines all available monitoring functions into one complete system overview.

---

## 📈 Development Roadmap

The project is being developed progressively, with each version introducing new Python and system-monitoring concepts.

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
├── Network Statistics
├── Bytes Sent
└── Bytes Received
```

**Status:** ✅ Complete

---

### V1.3 — Process Monitoring

```text
├── Running Processes
├── PID
├── Process Name
├── CPU Usage
└── Memory Usage
```

**Status:** ✅ Complete

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

Used to access system resources, network information, and running processes.

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
|               V1.3                |
-------------------------------------

1. CPU Usage
2. RAM Usage
3. Disk Usage
4. Full System Status
5. System Information
6. Network Information
7. Running Processes
8. Exit

Choose an option: 7

--- Running Processes ---

PID     Name            CPU%    Memory%

1234    explorer.exe    1.2     0.8
2456    python.exe      0.4     1.1
3789    chrome.exe      3.5     4.2
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

The structure will become more modular when the project moves toward **V2.0**.

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

## 🧠 What I Am Practicing

This project is helping me strengthen:

* Python Functions
* Control Flow
* Exception Handling
* Library Usage
* System Information
* Network Information
* Process Management
* Code Organization
* CLI Application Design

The goal is not only to make the program work, but to progressively improve its **architecture, readability, and functionality**.

---

## 🔮 Future Direction

The next major step is **V2.0**, where the project will move beyond a single-file procedural application.

Possible improvements include:

* [ ] Refactor the project using OOP
* [ ] Split the application into Modules
* [ ] Create dedicated Classes
* [ ] Add Logging
* [ ] Add JSON configuration
* [ ] Add Configuration management
* [ ] Improve error handling
* [ ] Improve process filtering
* [ ] Add detailed IP address information
* [ ] Add more detailed network monitoring
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
