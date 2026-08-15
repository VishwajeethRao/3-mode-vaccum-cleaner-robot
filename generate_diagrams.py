import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

os.makedirs('architecture', exist_ok=True)
os.makedirs('circuit', exist_ok=True)

# Remove legacy diagram if present
if os.path.exists('architecture/vacuum_mechanism_diagram.jpg'):
    os.remove('architecture/vacuum_mechanism_diagram.jpg')

# ---------------------------------------------------------
# 1. CLEAN SYSTEM ARCHITECTURE BLOCK DIAGRAM
# ---------------------------------------------------------
fig, ax = plt.subplots(figsize=(16, 12), dpi=200)
fig.patch.set_facecolor('#ffffff')
ax.set_facecolor('#ffffff')

# Title
ax.text(50, 96, '3-MODE VACUUM CLEANER ROBOT - SYSTEM ARCHITECTURE', 
        fontsize=20, fontweight='bold', ha='center', va='center', color='#0f172a')

# Helper function to draw rounded box
def draw_block(ax, x1, y1, x2, y2, title, subtitle="", bg="#f1f5f9", border="#475569", title_color="#0f172a", sub_color="#334155", title_size=12, sub_size=10):
    w = x2 - x1
    h = y2 - y1
    box = patches.FancyBboxPatch((x1, y1), w, h, boxstyle="round,pad=0,rounding_size=1.5",
                                 facecolor=bg, edgecolor=border, linewidth=2.5)
    ax.add_patch(box)
    if subtitle:
        ax.text(x1 + w/2, y1 + h*0.65, title, fontsize=title_size, fontweight='bold', ha='center', va='center', color=title_color)
        ax.text(x1 + w/2, y1 + h*0.30, subtitle, fontsize=sub_size, ha='center', va='center', color=sub_color)
    else:
        ax.text(x1 + w/2, y1 + h/2, title, fontsize=title_size, fontweight='bold', ha='center', va='center', color=title_color)

# Helper function for orthogonal connecting line with arrow
def draw_connection(ax, x1, y1, x2, y2, label="", color="#1e293b", lw=2.5, style="->"):
    ax.annotate(label, xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle=style, color=color, lw=lw, mutation_scale=15),
                fontsize=9, fontweight='bold', ha='center', va='center', color=color,
                bbox=dict(boxstyle="round,pad=0.3", fc="#ffffff", ec=color, lw=1) if label else None)

# --- BLOCKS LAYOUT ---
# 1. Top Power Box
draw_block(ax, 32, 84, 68, 92, "MAIN POWER SUPPLY", "Power / ON-OFF Switch", bg="#dbeafe", border="#2563eb", title_color="#1e40af", sub_color="#1d4ed8", title_size=13, sub_size=11)

# 2. Main Arduino Controller Box
draw_block(ax, 20, 64, 80, 76, "ARDUINO UNO MICROCONTROLLER", "Main Controller & System Logic (Mode-Specific Firmware Uploaded)", bg="#fef08a", border="#ca8a04", title_color="#854d0e", sub_color="#713f12", title_size=14, sub_size=11)

# Power Connection Arrow
draw_connection(ax, 50, 84, 50, 76, label="Main Power Input", color="#2563eb")

# 3. Column 1 (Left): Motor Driver & Motors
draw_block(ax, 4, 42, 34, 52, "L293D MOTOR DRIVER", "Dual H-Bridge Driver IC", bg="#e0e7ff", border="#4f46e5", title_color="#3730a3", sub_color="#4338ca", title_size=12, sub_size=10)
draw_block(ax, 4, 18, 34, 30, "4 × DC DRIVE MOTORS", "5 V, 200 RPM Geared Motors (4WD)", bg="#ecfdf5", border="#059669", title_color="#065f46", sub_color="#047857", title_size=12, sub_size=10)

draw_connection(ax, 27, 64, 19, 52, label="Control Signals", color="#4f46e5")
draw_connection(ax, 19, 42, 19, 30, label="Motor Drive Power", color="#059669")

# 4. Column 2 (Center): Ultrasonic Sensor
draw_block(ax, 38, 42, 62, 52, "HC-SR04 ULTRASONIC SENSOR", "Input Sensor (Obstacle Detection)", bg="#fce7f3", border="#db2777", title_color="#9d174d", sub_color="#be185d", title_size=12, sub_size=10)

draw_connection(ax, 50, 52, 50, 64, label="Distance Data", color="#db2777")

# 5. Column 3 (Right): Bluetooth & Mobile Application
draw_block(ax, 66, 42, 96, 52, "HC-05 BLUETOOTH MODULE", "Wireless Serial Communication", bg="#ffedd5", border="#ea580c", title_color="#9a3412", sub_color="#c2410c", title_size=12, sub_size=10)
draw_block(ax, 66, 16, 96, 32, "MOBILE APPLICATION", "• Voice Control Mode\n• Bluetooth / Mobile Control\n• Remote Control Mode", bg="#f3e8ff", border="#9333ea", title_color="#6b21a8", sub_color="#7e22ce", title_size=12, sub_size=10)

draw_connection(ax, 81, 64, 81, 52, label="Serial RX / TX", color="#ea580c")
draw_connection(ax, 81, 32, 81, 42, label="Bluetooth Commands", color="#9333ea", style="<->")

# 6. Bottom Box: Vacuum System Flow
draw_block(ax, 4, 3, 96, 11, "VACUUM CLEANING SYSTEM", "Arduino/Power Control  →  Vacuum Motor  →  Propeller/Fan  →  Suction  →  Garbage Collection Bottle + Mesh Filter", bg="#ccfbf1", border="#0d9488", title_color="#115e59", sub_color="#0f766e", title_size=11, sub_size=10)

ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

plt.tight_layout()
plt.savefig('architecture/block_diagram.jpg', dpi=200, bbox_inches='tight')
plt.close()
print('Generated clean architecture/block_diagram.jpg')


# ---------------------------------------------------------
# 2. CLEAN CIRCUIT SCHEMATIC BLOCK DIAGRAM
# ---------------------------------------------------------
fig, ax = plt.subplots(figsize=(16, 12), dpi=200)
fig.patch.set_facecolor('#ffffff')
ax.set_facecolor('#ffffff')

# Title
ax.text(50, 96, '3-MODE VACUUM CLEANER ROBOT - CIRCUIT SCHEMATIC DIAGRAM', 
        fontsize=20, fontweight='bold', ha='center', va='center', color='#0f172a')

# --- BLOCKS LAYOUT ---
# 1. Power Supply (Top Left)
draw_block(ax, 4, 80, 30, 92, "POWER SUPPLY &\nON/OFF SWITCH", "Main Power Control (Battery / Rail)", bg="#fee2e2", border="#ef4444", title_color="#991b1b", sub_color="#b91c1c", title_size=12, sub_size=10)

# 2. Arduino UNO (Top Center)
draw_block(ax, 37, 68, 63, 92, "ARDUINO UNO", "Main Microcontroller Board\n\n• Power Pins (Vin, 5V, GND)\n• Digital Pins (Motor Control)\n• Serial Pins (RX 0, TX 1)\n• Sensor Pins (Trig, Echo)", bg="#e0f2fe", border="#0284c7", title_color="#075985", sub_color="#0369a1", title_size=14, sub_size=10)

# 3. HC-SR04 Sensor (Top Right)
draw_block(ax, 70, 80, 96, 92, "HC-SR04 ULTRASONIC", "Obstacle Distance Sensor\n(VCC, Trig, Echo, GND)", bg="#fce7f3", border="#db2777", title_color="#9d174d", sub_color="#be185d", title_size=12, sub_size=10)

# 4. HC-05 Bluetooth (Middle Left)
draw_block(ax, 4, 44, 30, 58, "HC-05 BLUETOOTH", "Wireless Transceiver\n(VCC, GND, TXD, RXD)", bg="#ffedd5", border="#ea580c", title_color="#9a3412", sub_color="#c2410c", title_size=12, sub_size=10)

# 5. L293D Motor Driver (Middle Right)
draw_block(ax, 70, 44, 96, 58, "L293D MOTOR DRIVER", "Dual H-Bridge Driver\n(IN1-IN4, OUT1-OUT4)", bg="#fef3c7", border="#d97706", title_color="#78350f", sub_color="#92400e", title_size=12, sub_size=10)

# 6. Vacuum DC Motor (Bottom Left)
draw_block(ax, 4, 10, 44, 26, "VACUUM DC MOTOR & FAN", "Small DC Motor + Propeller\n(Connected to Power / Control Rail)", bg="#ccfbf1", border="#0d9488", title_color="#115e59", sub_color="#0f766e", title_size=12, sub_size=10)

# 7. 4 × DC Drive Motors (Bottom Right)
draw_block(ax, 56, 10, 96, 26, "4 × DC DRIVE MOTORS", "5 V, 200 RPM Geared Motors\n(Front-Left, Rear-Left, Front-Right, Rear-Right)", bg="#ecfdf5", border="#059669", title_color="#065f46", sub_color="#047857", title_size=12, sub_size=10)

# --- CLEAN NON-OVERLAPPING CONNECTIONS ---
# Power Supply -> Arduino
draw_connection(ax, 30, 86, 37, 86, label="Power Rail (VCC/GND)", color="#ef4444")

# Arduino -> HC-SR04
draw_connection(ax, 63, 86, 70, 86, label="Trig / Echo Pins", color="#db2777")

# Arduino -> HC-05 Bluetooth
draw_connection(ax, 37, 72, 17, 58, label="Arduino RX/TX ↔ HC-05 TX/RX", color="#ea580c", style="<->")

# Arduino -> L293D Motor Driver
draw_connection(ax, 63, 72, 83, 58, label="Arduino Digital Pins → L293D Inputs", color="#d97706")

# Power Supply -> Vacuum DC Motor
draw_connection(ax, 17, 80, 17, 26, label="Power Line to Vacuum Motor", color="#ef4444")

# L293D -> 4 DC Motors
draw_connection(ax, 83, 44, 83, 26, label="L293D Outputs (OUT1-OUT4) → Motors", color="#059669")

ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

plt.tight_layout()
plt.savefig('circuit/circuit_diagram.jpg', dpi=200, bbox_inches='tight')
plt.close()
print('Generated clean circuit/circuit_diagram.jpg')
