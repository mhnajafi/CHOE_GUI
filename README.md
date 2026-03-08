# Raspberry GUI Controller

This project implements a control system consisting of a Raspberry Pi-based graphical user interface (GUI) and an STM32 microcontroller backend. The system enables users to control hardware components (potentially motors or solenoids) via a touchscreen or mouse interface.

## Project Structure

The repository is divided into the following main components:

- **Raspberry Code/** (`program.py`):
    - A Python application using `tkinter` for the GUI.
    - Communicates with the microcontroller via Serial Port (`/dev/ttyUSB0` or similar).
    - Features buttons for selecting channels ("sel1" to "sel4") and controlling motors ("motor1", "motor2").
    - Implements threading for timer-based operations.

- **MCU Code/** (`CHOE/`):
    - Firmware for an STM32 microcontroller (STM32F1 series likely, based on file names).
    - Located in `MCU Code/CHOE/Src/main.c`.
    - Receives ASCII commands ('A', 'B', 'a', 'b', etc.) from the Raspberry Pi via UART (USART3).
    - Controls GPIO pins based on received commands to actuate connected hardware.

- **PCB/**:
    - Custom circuit board designs (`3CHOE.PcbDoc`, `3CHOE.PrjPcb`) created in Altium Designer.
    - Likely facilitates the connection between the STM32, the driver circuits, and the Raspberry Pi.

## Features

- **Intuitive Interface**: simple button-based control panel.
- **Serial Communication**: Robust UART link between the high-level OS (Raspberry Pi) and low-level hardware control (STM32).
- **Timed Operations**: Supports timed activation of channels (e.g., solenoid valves) via the GUI spinbox setting.
- **Toggle Control**: Motors/Outputs can be toggled on/off.

## Usage

1. **Hardware Setup**:
   - Connect the STM32 board to the Raspberry Pi via USB-Serial adapter or direct UART pins.
   - Power up the custom PCB.

2. **MCU Firmware**:
   - Open the project in `MCU Code/CHOE/` using STM32CubeIDE.
   - Compile and upload the code to the STM32 chip.

3. **Raspberry Pi**:
   - Ensure Python 3 and `pyserial` are installed (`pip3 install pyserial`).
   - Run the application:
     ```bash
     python3 "Raspberry Code/program.py"
     ```
   - Use the GUI to send commands.

