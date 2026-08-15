import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

os.makedirs('architecture', exist_ok=True)
os.makedirs('circuit', exist_ok=True)

# ---------------------------------------------------------
# 1. SYSTEM ARCHITECTURE BLOCK DIAGRAM
# ---------------------------------------------------------
fig, ax = plt.subplots(figsize=(14, 10), dpi=150)
fig.patch.set_facecolor('#f8fafc')
ax.set_facecolor('#f8fafc')

# Title
ax.text(0.5, 0.95, '3-MODE VACUUM CLEANER ROBOT - SYSTEM ARCHITECTURE', 
        fontsize=18, fontweight='bold', ha='center', va='center', color='#0f172a')

# Helper function to draw rounded box
def draw_box(ax, x, y, w, h, title, subtitle="", color="#e2e8f0", edgecolor="#64748b", textcolor="#0f172a", fontsize=11):
    box = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.03,rounding_size=0.04",
                                 facecolor=color, edgecolor=edgecolor, linewidth=2)
    ax.add_patch(box)
    if subtitle:
        ax.text(x + w/2, y + h*0.65, title, fontsize=fontsize, fontweight='bold', ha='center', va='center', color=textcolor)
        ax.text(x + w/2, y + h*0.3, subtitle, fontsize=fontsize-2, ha='center', va='center', color=textcolor, style='italic')
    else:
        ax.text(x + w/2, y + h/2, title, fontsize=fontsize, fontweight='bold', ha='center', va='center', color=textcolor)

# Helper function for arrows
def draw_arrow(ax, x1, y1, x2, y2, label="", color="#334155"):
    ax.annotate(label, xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="->", color=color, lw=2.5, mutation_scale=15),
                fontsize=9, fontweight='bold', ha='center', va='center', color=color)

# Top Power Box
draw_box(ax, 0.35, 0.82, 0.30, 0.08, "POWER SUPPLY", "Main ON / OFF Switch", color="#dbeafe", edgecolor="#2563eb", textcolor="#1e40af", fontsize=12)

# Central Controller Box
draw_box(ax, 0.32, 0.60, 0.36, 0.14, "MAIN CONTROLLER", "Arduino UNO Microcontroller\n(Mode-Specific Firmware Uploaded)", color="#fef08a", edgecolor="#ca8a04", textcolor="#854d0e", fontsize=12)

# Arrow Power -> Arduino
draw_arrow(ax, 0.50, 0.82, 0.50, 0.74, "Main Power Flow")

# Left: L293D & DC Motors
draw_box(ax, 0.03, 0.38, 0.26, 0.12, "MOTOR DRIVER", "L293D Dual H-Bridge Driver", color="#e0e7ff", edgecolor="#4f46e5", textcolor="#3730a3")
draw_box(ax, 0.03, 0.15, 0.26, 0.14, "DC DRIVE MOTORS", "4 × 5 V, 200 RPM Geared Motors\n(4WD Mobility)", color="#ecfdf5", edgecolor="#059669", textcolor="#065f46")

draw_arrow(ax, 0.32, 0.67, 0.29, 0.44, "Motor Control Signals")
draw_arrow(ax, 0.16, 0.38, 0.16, 0.29, "Driven Power Output")

# Center: Ultrasonic Sensor
draw_box(ax, 0.37, 0.38, 0.26, 0.12, "INPUT SENSOR", "HC-SR04 Ultrasonic Sensor\n(Obstacle Detection)", color="#fce7f3", edgecolor="#db2777", textcolor="#9d174d")

draw_arrow(ax, 0.50, 0.38, 0.50, 0.60, "Distance Echo / Trigger")

# Right: Bluetooth & Mobile App
draw_box(ax, 0.71, 0.38, 0.26, 0.12, "COMMUNICATION", "HC-05 Bluetooth Module", color="#ffedd5", edgecolor="#ea580c", textcolor="#9a3412")
draw_box(ax, 0.71, 0.10, 0.26, 0.20, "MOBILE APPLICATION", "• Voice Control Mode\n• Bluetooth / Mobile Control\n• Remote Control Mode", color="#f3e8ff", edgecolor="#9333ea", textcolor="#6b21a8")

draw_arrow(ax, 0.84, 0.38, 0.84, 0.60, "Serial RX / TX")
draw_arrow(ax, 0.84, 0.30, 0.84, 0.38, "Wireless Commands (2.4GHz)")

# Bottom Separate Box: Vacuum System Mechanism
draw_box(ax, 0.03, 0.02, 0.60, 0.09, "VACUUM CLEANING MECHANISM", "Arduino/Power Control → Vacuum DC Motor → Propeller/Fan → Air/Garbage Suction → Plastic Bottle → Mesh Filter", color="#ccfbf1", edgecolor="#0d9488", textcolor="#115e59", fontsize=10)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

plt.tight_layout()
plt.savefig('architecture/block_diagram.jpg', dpi=200, bbox_inches='tight')
plt.close()
print('Generated architecture/block_diagram.jpg successfully')


# ---------------------------------------------------------
# 2. CIRCUIT SCHEMATIC DIAGRAM
# ---------------------------------------------------------
fig, ax = plt.subplots(figsize=(15, 11), dpi=150)
fig.patch.set_facecolor('#ffffff')
ax.set_facecolor('#ffffff')

ax.text(0.5, 0.96, '3-MODE VACUUM CLEANER ROBOT - CIRCUIT SCHEMATIC DIAGRAM', 
        fontsize=18, fontweight='bold', ha='center', va='center', color='#0f172a')

# Helper function to draw block with pin labels
def draw_chip(ax, x, y, w, h, name, pins_left=[], pins_right=[], pins_top=[], pins_bottom=[], bg="#ffffff", border="#000000"):
    chip = patches.FancyBboxPatch((x, y), w, h, boxstyle="square,pad=0", facecolor=bg, edgecolor=border, linewidth=2)
    ax.add_patch(chip)
    ax.text(x + w/2, y + h/2, name, fontsize=12, fontweight='bold', ha='center', va='center', color="#0f172a")
    
    # Left pins
    if pins_left:
        step = h / (len(pins_left) + 1)
        for i, pin in enumerate(pins_left):
            py = y + h - (i + 1) * step
            ax.plot([x - 0.02, x], [py, py], color="#000000", lw=1.5)
            ax.text(x + 0.01, py, pin, fontsize=8, ha='left', va='center', fontweight='bold')
            
    # Right pins
    if pins_right:
        step = h / (len(pins_right) + 1)
        for i, pin in enumerate(pins_right):
            py = y + h - (i + 1) * step
            ax.plot([x + w, x + w + 0.02], [py, py], color="#000000", lw=1.5)
            ax.text(x + w - 0.01, py, pin, fontsize=8, ha='right', va='center', fontweight='bold')
            
    # Top pins
    if pins_top:
        step = w / (len(pins_top) + 1)
        for i, pin in enumerate(pins_top):
            px = x + (i + 1) * step
            ax.plot([px, px], [y + h, y + h + 0.02], color="#000000", lw=1.5)
            ax.text(px, y + h - 0.01, pin, fontsize=8, ha='center', va='top', fontweight='bold')

# Arduino UNO (Center Left)
draw_chip(ax, 0.30, 0.35, 0.22, 0.45, "ARDUINO UNO\n(Main Controller)",
          pins_left=["Vin", "5V", "GND", "Power Switch In"],
          pins_right=["Digital Pins (Motor Ctrl)", "Trig Pin", "Echo Pin", "RX (Pin 0)", "TX (Pin 1)", "Vacuum Ctrl Pin"],
          bg="#e0f2fe", border="#0284c7")

# L293D Motor Driver (Center Right)
draw_chip(ax, 0.65, 0.45, 0.18, 0.35, "L293D MOTOR DRIVER",
          pins_left=["IN1 / IN2 (Left)", "IN3 / IN4 (Right)", "EN1 / EN2", "VCC / GND"],
          pins_right=["OUT1", "OUT2", "OUT3", "OUT4"],
          bg="#fef3c7", border="#d97706")

# 4 Motors (Far Right)
draw_box(ax, 0.87, 0.72, 0.11, 0.09, "M1: 5V DC Motor\n(Front-Left 200 RPM)", color="#ecfdf5", edgecolor="#10b981", fontsize=8)
draw_box(ax, 0.87, 0.60, 0.11, 0.09, "M2: 5V DC Motor\n(Rear-Left 200 RPM)", color="#ecfdf5", edgecolor="#10b981", fontsize=8)
draw_box(ax, 0.87, 0.48, 0.11, 0.09, "M3: 5V DC Motor\n(Front-Right 200 RPM)", color="#ecfdf5", edgecolor="#10b981", fontsize=8)
draw_box(ax, 0.87, 0.36, 0.11, 0.09, "M4: 5V DC Motor\n(Rear-Right 200 RPM)", color="#ecfdf5", edgecolor="#10b981", fontsize=8)

# HC-SR04 Ultrasonic Sensor (Top Left)
draw_chip(ax, 0.03, 0.70, 0.18, 0.18, "HC-SR04 ULTRASONIC\n(Obstacle Sensor)",
          pins_right=["VCC (+5V)", "Trig (Input)", "Echo (Output)", "GND"],
          bg="#fce7f3", border="#ec4899")

# HC-05 Bluetooth Module (Bottom Left)
draw_chip(ax, 0.03, 0.38, 0.18, 0.18, "HC-05 BLUETOOTH\n(Wireless Serial)",
          pins_right=["VCC (+5V)", "GND", "TXD (Transmit)", "RXD (Receive)"],
          bg="#ffedd5", border="#f97316")

# Main ON/OFF Power Switch (Bottom Center)
draw_box(ax, 0.03, 0.10, 0.22, 0.14, "POWER SUPPLY &\nON/OFF SWITCH", "Battery Pack / Power Rail\nMain Power Interrupter", color="#fee2e2", edgecolor="#ef4444", textcolor="#b91c1c", fontsize=9)

# Vacuum DC Motor (Bottom Right)
draw_box(ax, 0.65, 0.10, 0.25, 0.18, "VACUUM SYSTEM MOTOR", "Small DC Motor + Propeller/Fan\nConnected via Power / Arduino Control Rail", color="#ccfbf1", edgecolor="#14b8a6", textcolor="#0f766e", fontsize=9)

# Connection lines
# Arduino -> L293D
ax.annotate("", xy=(0.65, 0.72), xytext=(0.52, 0.72), arrowprops=dict(arrowstyle="->", color="#2563eb", lw=2))
ax.text(0.585, 0.74, "Arduino Digital Pins → L293D Inputs", fontsize=8, fontweight='bold', ha='center', color="#1d4ed8")

# L293D -> Motors
ax.annotate("", xy=(0.87, 0.76), xytext=(0.83, 0.76), arrowprops=dict(arrowstyle="->", color="#059669", lw=1.5))
ax.annotate("", xy=(0.87, 0.64), xytext=(0.83, 0.64), arrowprops=dict(arrowstyle="->", color="#059669", lw=1.5))
ax.annotate("", xy=(0.87, 0.52), xytext=(0.83, 0.52), arrowprops=dict(arrowstyle="->", color="#059669", lw=1.5))
ax.annotate("", xy=(0.87, 0.40), xytext=(0.83, 0.40), arrowprops=dict(arrowstyle="->", color="#059669", lw=1.5))

# HC-SR04 -> Arduino
ax.annotate("", xy=(0.30, 0.65), xytext=(0.21, 0.75), arrowprops=dict(arrowstyle="<-", color="#db2777", lw=2))
ax.text(0.24, 0.72, "Trig / Echo Pins", fontsize=8, fontweight='bold', ha='center', color="#9d174d")

# HC-05 -> Arduino
ax.annotate("", xy=(0.30, 0.47), xytext=(0.21, 0.47), arrowprops=dict(arrowstyle="<->", color="#ea580c", lw=2))
ax.text(0.25, 0.49, "Arduino RX/TX ↔ HC-05 TX/RX", fontsize=8, fontweight='bold', ha='center', color="#c2410c")

# Power Switch -> Arduino & L293D
ax.annotate("", xy=(0.35, 0.35), xytext=(0.25, 0.24), arrowprops=dict(arrowstyle="->", color="#dc2626", lw=2))
ax.text(0.33, 0.27, "VCC Power Rail (ON/OFF Switch)", fontsize=8, fontweight='bold', ha='center', color="#b91c1c")

ax.annotate("", xy=(0.70, 0.28), xytext=(0.70, 0.45), arrowprops=dict(arrowstyle="<-", color="#dc2626", lw=1.5))
ax.annotate("", xy=(0.77, 0.28), xytext=(0.40, 0.20), arrowprops=dict(arrowstyle="->", color="#0d9488", lw=2))
ax.text(0.55, 0.22, "Power / Arduino Control Line to Vacuum Motor", fontsize=8, fontweight='bold', ha='center', color="#0f766e")

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

plt.tight_layout()
plt.savefig('circuit/circuit_diagram.jpg', dpi=200, bbox_inches='tight')
plt.close()
print('Generated circuit/circuit_diagram.jpg successfully')


# ---------------------------------------------------------
# 3. VACUUM MECHANISM DIAGRAM
# ---------------------------------------------------------
fig, ax = plt.subplots(figsize=(14, 8), dpi=150)
fig.patch.set_facecolor('#ffffff')
ax.set_facecolor('#ffffff')

ax.text(0.5, 0.93, 'BOTTLE-BASED VACUUM CLEANER MECHANISM', 
        fontsize=18, fontweight='bold', ha='center', va='center', color='#0f172a')
ax.text(0.5, 0.88, 'Modified Plastic Bottle Chamber with Small DC Motor, Propeller Fan & Mesh Filter', 
        fontsize=11, ha='center', va='center', color='#475569', style='italic')

# Draw Plastic Bottle Contour
bottle_x = [0.15, 0.20, 0.65, 0.75, 0.75, 0.65, 0.20, 0.15, 0.15]
bottle_y = [0.25, 0.20, 0.20, 0.35, 0.65, 0.80, 0.80, 0.75, 0.25]
ax.plot(bottle_x, bottle_y, color='#0284c7', lw=3, label='Inverted Plastic Bottle Chamber')

# Fill Bottle Interior
ax.fill(bottle_x, bottle_y, color='#e0f2fe', alpha=0.5)

# Mesh Filter (Vertical barrier across bottle opening/middle)
ax.plot([0.22, 0.22], [0.20, 0.80], color='#d97706', lw=4, linestyle='--', label='Mesh Filter (Retains Debris)')
ax.text(0.22, 0.84, 'Mesh Filter Cover\n(Passes Air, Blocks Garbage)', fontsize=9, fontweight='bold', ha='center', color='#b45309')

# Front Suction Inlet
ax.annotate("Suction Inlet\n(Pulls Air & Garbage)", xy=(0.15, 0.50), xytext=(0.02, 0.50),
            arrowprops=dict(arrowstyle="->", color="#0284c7", lw=3, mutation_scale=20),
            fontsize=10, fontweight='bold', ha='center', va='center', color="#0369a1")

# Debris Particles inside collection chamber
import numpy as np
np.random.seed(42)
debris_x = np.random.uniform(0.25, 0.58, 25)
debris_y = np.random.uniform(0.25, 0.75, 25)
ax.scatter(debris_x, debris_y, color='#b45309', s=40, zorder=5, label='Collected Garbage / Dust')

# Rear DC Motor & Propeller
draw_box(ax, 0.77, 0.40, 0.12, 0.20, "Small DC Motor", "High-RPM", color="#fee2e2", edgecolor="#ef4444", textcolor="#991b1b", fontsize=9)
# Propeller fan inside rear neck
ax.plot([0.70, 0.70], [0.36, 0.64], color='#dc2626', lw=4, label='Propeller / Fan')
ax.plot([0.67, 0.73], [0.40, 0.60], color='#dc2626', lw=2)
ax.plot([0.67, 0.73], [0.60, 0.40], color='#dc2626', lw=2)
ax.text(0.70, 0.68, 'Rotating Propeller / Fan\n(Generates Low Pressure)', fontsize=9, fontweight='bold', ha='center', color='#b91c1c')

# Airflow Arrows through system
ax.annotate("", xy=(0.35, 0.50), xytext=(0.20, 0.50), arrowprops=dict(arrowstyle="->", color="#0284c7", lw=2.5))
ax.annotate("", xy=(0.60, 0.50), xytext=(0.45, 0.50), arrowprops=dict(arrowstyle="->", color="#0284c7", lw=2.5))
ax.annotate("Exhaust Air", xy=(0.95, 0.50), xytext=(0.89, 0.50), arrowprops=dict(arrowstyle="->", color="#059669", lw=2.5, mutation_scale=18), fontsize=10, fontweight='bold', ha='center', color="#047857")

# Garbage Retention Callout Box
draw_box(ax, 0.30, 0.05, 0.35, 0.12, "GARBAGE COLLECTION CHAMBER", "Air is drawn in through suction → Debris retained by mesh → Air exhausts out rear", color="#fef3c7", edgecolor="#f59e0b", textcolor="#78350f", fontsize=9)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

plt.tight_layout()
plt.savefig('architecture/vacuum_mechanism_diagram.jpg', dpi=200, bbox_inches='tight')
plt.close()
print('Generated architecture/vacuum_mechanism_diagram.jpg successfully')
