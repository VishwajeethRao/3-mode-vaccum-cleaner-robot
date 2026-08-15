# 3-Mode Autonomous Vacuum Cleaner Robot (Autonomous, Bluetooth & Voice Control)

An intelligent, multi-mode hardware prototype for an automated vacuum cleaning robot built with Arduino UNO. The system combines autonomous obstacle avoidance, manual Bluetooth app navigation, and voice command recognition to deliver efficient, hands-free indoor cleaning.

---

## 📖 Short Description

This project features a 4-wheel drive robotic vacuum cleaner controlled by an Arduino UNO microcontroller. It is designed to clean indoor floor surfaces through three operating modes: **Autonomous Obstacle Avoidance**, **Manual Bluetooth App Control**, and **Hands-free Voice Command Integration**. Equipped with a mini vacuum suction module, HC-SR04 ultrasonic distance sensor mounted on an SG90 servo motor, and an HC-05 Bluetooth module, the robot offers an affordable, customizable alternative to commercial robotic vacuum cleaners.

---

## 🎯 Problem Solved

Traditional household floor cleaning is time-consuming, physically demanding, and requires continuous human supervision. While commercial robotic vacuum cleaners exist, they are often expensive, proprietary, and lack customizable control options. 

This project addresses these challenges by:
- Automating repetitive floor cleaning tasks to save time and manual effort.
- Providing multiple control options (autonomous navigation, smartphone app control, and voice interaction) suitable for diverse user needs, including working professionals and individuals with mobility constraints.
- Offering a low-cost, open-hardware DIY platform suitable for educational demonstrations, embedded robotics research, and home automation applications.

---

## ✨ Main Features

- **Multi-Mode Operation**:
  - **Autonomous Obstacle Avoidance Mode**: Self-navigating floor cleaning using real-time ultrasonic distance scanning to detect obstacles within 12 cm and dynamically re-route the robot.
  - **Bluetooth Control Mode**: Manual direction control (Forward, Backward, Left, Right, Stop) operated wirelessly via a smartphone application connected to an HC-05 Bluetooth module.
  - **Voice Control Mode**: Hands-free movement execution based on recognized speech strings ("forward", "backward", "left", "right", "stop").
- **Integrated Cleaning System**: Onboard mini vacuum motor / suction fan and dustbin for debris collection.
- **Dynamic Servo Scanning**: SG90 servo motor rotates the HC-SR04 ultrasonic sensor left (180°) and right (20°) to sweep and identify the clearest path when obstacles are encountered.
- **4-Wheel Drive Mobility**: Driven by 4 DC motors paired with an Adafruit Motor Shield / L293D motor driver module for smooth indoor navigation.

---

## 🛠️ Components Used

| Component | Quantity | Description / Specifications |
| :--- | :---: | :--- |
| **Arduino UNO** | 1 | ATmega328P based microcontroller board |
| **Adafruit Motor Shield (L293D)** | 1 | Dual H-Bridge motor driver shield for controlling 4 DC motors & servo |
| **HC-SR04 Ultrasonic Sensor** | 1 | Distance sensor (2cm - 400cm range) for obstacle detection |
| **SG90 Micro Servo Motor** | 1 | Positional servo for rotating the ultrasonic sensor (180° sweep) |
| **HC-05 Bluetooth Module** | 1 | Wireless serial communication module (baud rate 9600) |
| **Mini Vacuum Motor / Suction Fan** | 1 | Onboard suction mechanism for dust collection |
| **BO Motors with Wheels** | 4 | Geared DC motors for 4WD movement |
| **Li-ion Battery Pack / Power Source** | 1 | Rechargeable power supply (7.4V / 12V) |
| **Robot Chassis** | 1 | Custom lightweight chassis with dustbin compartment |
| **Power Switch & Jumper Wires** | As required | SPST switch, male-to-male jumper cables, and breadboard |

---

## ⚡ Working Principle

1. **Control Unit & Sensing**:
   - The **Arduino UNO** acts as the main controller.
   - In **Autonomous Mode**, the **HC-SR04 ultrasonic sensor** continuously measures the distance to obstacles in front of the robot.
   - If an obstacle is detected within **12 cm**, the robot halts, moves backward briefly, and signals the **SG90 servo motor** to rotate left (`180°`) and right (`20°`) to evaluate distances in both directions.
   - The microcontroller compares the left and right clearance readings, turns the robot toward the clearer side, and resumes forward cleaning motion.

2. **Wireless Communication**:
   - In **Bluetooth Control Mode**, the **HC-05 module** listens for serial commands from a paired mobile app. Characters `'F'`, `'B'`, `'L'`, `'R'`, and `'S'` trigger forward, backward, left, right, and stop motor states respectively.
   - In **Voice Control Mode**, received serial text strings ("forward", "backward", "left", "right", "stop") are parsed by the Arduino. For turn commands, the robot inspects space using the ultrasonic sensor before moving to ensure safe maneuvering.

3. **Suction & Cleaning**:
   - The onboard suction fan runs continuously during operation to pull dust and fine particles into the onboard collection bin while the robot navigates the floor.

---

## 📐 System Architecture & Circuit Diagram

### System Block Diagram
![Block Diagram](architecture/block_diagram.jpg)

### Circuit Diagram
![Circuit Diagram](circuit/circuit_diagram.jpg)

---

## 🖼️ Hardware Gallery & Demonstration

### Prototype Photos
| Front & Sensor View | Side Profile | Suction Chamber |
| :---: | :---: | :---: |
| ![Front Sensor View](photos/ultrasonic_sensor_mount.jpg) | ![Side Profile](photos/robot_side_profile.jpg) | ![Suction Chamber](photos/suction_chamber_top_view.jpg) |

| Perspective View | Top Front View | Chassis Structure |
| :---: | :---: | :---: |
| ![Perspective View](photos/robot_perspective_view.jpg) | ![Top Front View](photos/robot_top_front_view.jpg) | ![Chassis Structure](photos/chassis_structure_view.jpg) |

### Demo Videos
Demonstration videos showing the physical robot prototype in action are available in the [`video/`](video/) directory:
- [`video/robot_demo_full.mp4`](video/robot_demo_full.mp4) - Complete operational demonstration
- [`video/robot_demo_short.mp4`](video/robot_demo_short.mp4) - Quick functional highlight

---

## 🚀 Basic Setup & Usage

### 1. Hardware Assembly
- Connect the **Adafruit Motor Shield** onto the **Arduino UNO**.
- Wire the 4 BO DC motors to motor channels M1, M2, M3, and M4 on the shield.
- Connect the **SG90 Servo Motor** signal pin to Digital Pin `10`.
- Connect the **HC-SR04 Ultrasonic Sensor** `Trig` to Analog Pin `A1` and `Echo` to Analog Pin `A0`.
- Connect the **HC-05 Bluetooth Module** `TX` to Arduino `RX` (Pin 0) and `RX` to Arduino `TX` (Pin 1).
- Connect the rechargeable battery pack through the main power switch to power both the Arduino and motor shield.

### 2. Software Requirements
- **Arduino IDE** (v1.8.x or v2.x)
- Required Libraries:
  - `AFMotor.h` (Adafruit Motor Shield library)
  - `Servo.h` (Standard Arduino Servo library)

### 3. Code Upload & Mode Configuration
1. Open [`code/vaccum.ino`](code/vaccum.ino) in the Arduino IDE.
2. Select **Board**: `Arduino Uno` and choose your serial **Port**.
3. In `loop()`, select your desired operating mode by uncommenting the corresponding function:
   ```cpp
   void loop() {
     // Obstacle();           // Enable for Autonomous Obstacle Avoidance
     Bluetoothcontrol();      // Enable for Mobile App Bluetooth Control
     // voicecontrol();       // Enable for Voice Command Control
   }
   ```
4. Temporarily disconnect the HC-05 `TX`/`RX` pins while uploading code via USB to avoid serial port conflict.
5. Click **Upload**. Reconnect HC-05 after upload completes.

---

## 🧰 Tools & Software Used

- **Embedded Firmware**: C / C++ (Arduino Framework)
- **IDE**: Arduino IDE
- **Libraries**: `AFMotor.h`, `Servo.h`
- **Design & Circuit Analysis**: Fritzing / System Schematics
- **Mobile Control**: Bluetooth Serial Terminal / Bluetooth RC Controller App

---

## 📁 Repository Structure

```text
.
├── README.md                                          # Comprehensive project documentation
├── architecture/
│   └── block_diagram.jpg                             # System architecture block diagram
├── circuit/
│   └── circuit_diagram.jpg                           # Hardware wiring and schematic diagram
├── code/
│   └── vaccum.ino                                    # Provided Arduino UNO source code
├── photos/
│   ├── chassis_structure_view.jpg                    # Base chassis structural photo
│   ├── power_switch_assembly.jpg                     # Power switch detail photo
│   ├── robot_perspective_view.jpg                    # Complete robot perspective photo
│   ├── robot_side_profile.jpg                        # Side profile photo
│   ├── robot_top_front_view.jpg                      # Top-front view photo
│   ├── suction_chamber_top_view.jpg                  # Suction fan & dust collector photo
│   └── ultrasonic_sensor_mount.jpg                   # Front ultrasonic sensor mount photo
├── video/
│   ├── robot_demo_full.mp4                           # Full project video demonstration
│   └── robot_demo_short.mp4                          # Short video clip
└── autonomous vaccum cleaner robot...pdf              # Original project documentation report
```
