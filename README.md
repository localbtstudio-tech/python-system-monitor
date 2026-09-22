# PYTHON SYSTEM MONITOR 🖥️

<p align="center">
  <strong>A modular command-line system monitoring tool built with Python.</strong>
</p>

<p align="center">
  <strong>Python · OOP · Modules · JSON · Logging · psutil · CLI</strong>
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python\&logoColor=white)
![psutil](https://img.shields.io/badge/psutil-System%20Monitoring-orange)
![OOP](https://img.shields.io/badge/OOP-Object%20Oriented-purple)
![JSON](https://img.shields.io/badge/Config-JSON-yellow)
![Logging](https://img.shields.io/badge/Logging-Enabled-green)
![Version](https://img.shields.io/badge/Version-2.0-red)
![Status](https://img.shields.io/badge/Status-In%20Development-yellow)

</p>

---

## ◼︎ Project Overview

**Python System Monitor** is a command-line system monitoring application built with Python and `psutil`.

The project started as a simple procedural Python application and evolved into a more structured **V2.0 architecture** using:

* Object-Oriented Programming
* Python Modules
* JSON Configuration
* Logging
* Configurable settings
* Process monitoring
* System monitoring

The goal of V2.0 is not only to monitor the system, but also to practice building a **cleaner and more maintainable Python application**.

---

## ✦ V2.0 Features

```text
PYTHON SYSTEM MONITOR V2.0
│
├── CPU Usage
├── RAM Usage
├── Disk Usage
├── Full System Status
├── System Information
├── Network Information
├── Running Processes
│
├── OOP Architecture
├── Modular Structure
├── JSON Configuration
└── Application Logging
```

---

# ⚙️ Application Menu

```text
-------------------------------------
|        PYTHON SYSTEM MONITOR      |
|               V2.0                |
-------------------------------------

1. CPU Usage
2. RAM Usage
3. Disk Usage
4. Full System Status
5. System Information
6. Network Information
7. Running Processes
8. Exit
```

---

# 🧠 V2.0 Architecture

Unlike V1.3, where most of the application existed inside `main.py`, V2.0 separates responsibilities into different files.

```text
                    ┌─────────────────────┐
                    │      main.py        │
                    │  Application Entry  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   config.json       │
                    │   Configuration     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  SystemMonitor      │
                    │      Class           │
                    └──────────┬──────────┘
                               │
          ┌────────────────────┼────────────────────┐
          ▼                    ▼                    ▼
      CPU / RAM            Network              Processes
      Disk Usage           Information          Monitoring
          │                    │                    │
          └────────────────────┼────────────────────┘
                               ▼
                    ┌─────────────────────┐
                    │   system_monitor.log│
                    │      Logging        │
                    └─────────────────────┘
```

---

# 🏗️ Object-Oriented Programming

V2.0 introduces a `SystemMonitor` class.

```python
class SystemMonitor:

    def __init__(self, config):
        self.config = config
```

The application then creates an object:

```python
monitor = SystemMonitor(config)
```

The monitoring functions are now **Methods** of the class:

```python
monitor.cpu_usage()
monitor.ram_usage()
monitor.disk_usage()
monitor.process_information()
```

This replaces the procedural structure used in earlier versions.

### V1.3

```text
cpu_usage()
ram_usage()
disk_usage()
```

### V2.0

```text
monitor.cpu_usage()
monitor.ram_usage()
monitor.disk_usage()
```

---

# 📦 Modules

The application is now separated into multiple Python files.

```text
python-system-monitor/
│
├── main.py
│
├── system_monitor.py
│
├── config.json
│
└── system_monitor.log
```

`main.py` handles the application flow.

`system_monitor.py` contains the `SystemMonitor` class and monitoring logic.

This separation makes the project easier to understand, maintain and extend.

---

# ⚙️ Configuration

V2.0 introduces an external `config.json` file.

```json
{
    "app_name": "PYTHON SYSTEM MONITOR",
    "version": "V2.0",
    "cpu_delay": 1,
    "process_limit": 20,
    "log_file": "system_monitor.log"
}
```

Instead of hardcoding configuration values inside Python, the application loads them from JSON.

For example:

```python
self.cpu_delay = config["cpu_delay"]
self.process_limit = config["process_limit"]
```

This means configuration can be changed without modifying the main Python logic.

---

# 🗂️ Configuration Options

| Setting         | Description                  |
| --------------- | ---------------------------- |
| `app_name`      | Application name             |
| `version`       | Current application version  |
| `cpu_delay`     | Delay before CPU measurement |
| `process_limit` | Maximum processes displayed  |
| `log_file`      | Logging output file          |

Example:

```text
process_limit = 20
```

Changing it to:

```text
process_limit = 50
```

allows the application to display up to 50 processes.

---

# 📊 System Monitoring

## CPU Usage

Uses:

```python
psutil.cpu_percent()
```

Displays the current CPU utilization.

---

## RAM Usage

Uses:

```python
psutil.virtual_memory()
```

Displays the current RAM utilization percentage.

---

## Disk Usage

Uses:

```python
psutil.disk_usage("/")
```

Displays disk usage information.

---

# 🖥️ System Information

The application collects information about the operating system.

```text
OS
OS Version
Architecture
CPU Cores
Hostname
```

Technologies used:

```python
platform.system()
platform.version()
platform.machine()
platform.node()
psutil.cpu_count()
```

---

# 🌐 Network Information

The application collects network interface and traffic information.

```python
psutil.net_if_addrs()
psutil.net_io_counters()
```

Current information includes:

```text
Network Interfaces
Bytes Sent
Bytes Received
```

---

# 🔍 Process Monitoring

V2.0 continues the process monitoring system introduced in V1.3.

Processes are retrieved using:

```python
psutil.process_iter(
    ["pid", "name", "cpu_percent", "memory_percent"]
)
```

The application displays:

```text
PID
Process Name
CPU Usage
Memory Usage
```

A configurable process limit is also introduced:

```python
self.process_limit
```

The application handles processes that disappear or cannot be accessed:

```python
except (psutil.NoSuchProcess, psutil.AccessDenied):
    continue
```

---

# 📝 Logging

V2.0 introduces application logging.

Logging is configured in `main.py`:

```python
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
```

The application records important events such as:

```text
Application started
Checking CPU usage
CPU usage: 27.40%
Checking RAM usage
Checking running processes
Application closed
```

Example:

```text
2026-09-22 18:40:12,120 - INFO - Application started
2026-09-22 18:40:15,341 - INFO - Checking CPU usage
2026-09-22 18:40:16,344 - INFO - CPU usage: 27.40%
2026-09-22 18:40:20,110 - INFO - Checking running processes
```

The log file is generated automatically:

```text
system_monitor.log
```

---

# 🧩 Main Components

```text
main.py
│
├── load_config()
│       └── Reads config.json
│
├── setup_logging()
│       └── Configures application logging
│
├── display_menu()
│       └── Displays CLI menu
│
└── main()
        │
        ├── Load Configuration
        ├── Setup Logging
        ├── Create SystemMonitor Object
        │
        └── Main Program Loop
                │
                ├── CPU
                ├── RAM
                ├── Disk
                ├── Full Status
                ├── System Information
                ├── Network Information
                └── Processes
```

---

# 🧱 SystemMonitor Class

```text
SystemMonitor
│
├── __init__()
│
├── cpu_usage()
├── ram_usage()
├── disk_usage()
├── system_information()
├── network_information()
├── process_information()
└── full_system_status()
```

The class stores configuration using:

```python
self.config
```

and exposes configuration values through attributes such as:

```python
self.cpu_delay
self.process_limit
```

---

# 📚 Concepts Practiced

| Concept        | Status |
| -------------- | ------ |
| Variables      | ✅      |
| Conditions     | ✅      |
| Loops          | ✅      |
| Functions      | ✅      |
| Error Handling | ✅      |
| `psutil`       | ✅      |
| Modules        | ✅      |
| OOP            | ✅      |
| Classes        | ✅      |
| Objects        | ✅      |
| `self`         | ✅      |
| Methods        | ✅      |
| JSON           | ✅      |
| Configuration  | ✅      |
| Logging        | ✅      |
| CLI            | ✅      |

---

# 🗺️ Version History

```text
V1.0
 │
 ├── CPU Monitoring
 ├── RAM Monitoring
 ├── Disk Monitoring
 └── Full System Status
 │
 ▼
V1.1
 │
 ├── OS Information
 ├── Architecture
 ├── CPU Cores
 └── Hostname
 │
 ▼
V1.2
 │
 ├── Network Interfaces
 ├── Bytes Sent
 └── Bytes Received
 │
 ▼
V1.3
 │
 ├── Running Processes
 ├── PID
 ├── CPU Usage
 ├── Memory Usage
 └── Process Error Handling
 │
 ▼
V2.0
 │
 ├── OOP
 ├── Classes
 ├── Objects
 ├── Modules
 ├── JSON
 ├── Configuration
 └── Logging
```

---

# 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/localbtstudio-tech/python-system-monitor.git
```

### 2. Enter the project directory

```bash
cd python-system-monitor
```

### 3. Install the dependency

```bash
pip install psutil
```

### 4. Run the application

```bash
python main.py
```

---

# 💻 Example

```text
-------------------------------------
|        PYTHON SYSTEM MONITOR      |
|               V2.0                |
-------------------------------------

1. CPU Usage
2. RAM Usage
3. Disk Usage
4. Full System Status
5. System Information
6. Network Information
7. Running Processes
8. Exit

Choose an option: 1

Measuring CPU...
CPU Usage: 27.4 %
```

---

# 📁 Project Structure

```text
python-system-monitor/
│
├── main.py
│
├── system_monitor.py
│
├── config.json
│
├── README.md
│
├── .gitignore
│
└── system_monitor.log
```

> `system_monitor.log` is generated automatically when the application runs.

---

# 🎯 Why I Built This

This project is part of my journey to strengthen my **Python programming and cybersecurity foundations**.

The project started as a simple system monitoring script and gradually evolved into a more structured application.

```text
Python Basics
      │
      ▼
Functions
      │
      ▼
psutil
      │
      ▼
System Monitoring
      │
      ▼
OOP
      │
      ▼
Modules
      │
      ▼
JSON + Configuration
      │
      ▼
Logging
      │
      ▼
Cybersecurity Projects
```

The main goal is to understand how Python concepts can be combined to build increasingly realistic software projects.

---

# 🔮 Future Direction

The next major project will move from **system monitoring** toward **cybersecurity log analysis**.

```text
System Monitor
      │
      ▼
Log Parser
      │
      ▼
IOC Checker
      │
      ▼
Log Analyzer
      │
      ▼
Threat Intelligence Automation
```

Future improvements for this project may include:

* Detailed IP address information
* Advanced network monitoring
* More detailed process analysis
* Better logging and error handling
* Automated JSON reports
* GUI / Dashboard
* Configuration validation

---

# 🛠️ Technologies

* **Python 3**
* **psutil**
* **platform**
* **OOP**
* **JSON**
* **Logging**
* **CLI**

---

# 👨‍💻 Author

**Hamza Weslati**

IT Student · Web Developer · Software Development

<p align="left">

<a href="https://github.com/localbtstudio-tech">
<img src="https://img.shields.io/badge/GitHub-localbtstudio--tech-black?logo=github">
</a>

<a href="https://www.linkedin.com/in/hamza-weslati-9a99a8419/">
<img src="https://img.shields.io/badge/LinkedIn-Hamza%20Weslati-blue?logo=linkedin">
</a>

</p>

---

<p align="center">
  <strong>Python System Monitor V2.0</strong><br>
  Built to learn. Built to improve. Built with Python.
</p>
