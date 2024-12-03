# Real-Time Port Monitor

A Python program that tracks network port activity in real-time, logging newly opened and closed ports with process details.

## Features
- **Live Monitoring**: Detects newly opened and closed ports.
- **Process Info**: Shows the process name and PID for opened ports.
- **Stylish Output**: Uses colors and ASCII art for an aesthetic interface.

## How It Works
- Monitors system network connections using `psutil`.
- Compares current and previous states to detect changes.
- Logs activity with color-coded messages.

## Usage
Run the script to monitor your system's network activity in real-time.
