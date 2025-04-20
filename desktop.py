import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize

# Simulated app icons
def load_icons():
    # Get the path to the user's Desktop
    desktop_path = os.path.expanduser('~/Desktop')

    # Check if Desktop exists
    if not os.path.exists(desktop_path):
        return []

    icons = []

    # Iterate over the files on the Desktop
    for filename in os.listdir(desktop_path):
        file_path = os.path.join(desktop_path, filename)

        # Check if it's a valid .desktop file (optional filter)
        if filename.endswith('.desktop'):
            # Read the .desktop file
            with open(file_path, 'r') as f:
                content = f.readlines()
            
            # Extract the name, icon, and command (simplified)
            name = None
            icon = None
            exec_cmd = None
            for line in content:
                if line.startswith('Name='):
                    name = line.strip().split('=')[1]
                elif line.startswith('Icon='):
                    icon = line.strip().split('=')[1]
                elif line.startswith('Exec='):
                    exec_cmd = line.strip().split('=')[1]

            if name and exec_cmd:  # Only add if name and exec_cmd are available
                icon_path = icon if icon else "/usr/share/icons/hicolor/128x128/apps/default-icon.png"  # Fallback icon
                icons.append({
                    "name": name,
                    "icon": icon_path,
                    "exec": exec_cmd
                })
        else:
            icons.append({
                "name": filename,
                "icon": "assets/icons/config.svg",
                "exec": ""
            })

    return icons

app = QApplication(sys.argv)

# Create the main window (desktop)
desktop = QWidget()
desktop.setWindowFlags(Qt.FramelessWindowHint)  # No borders, always on top
desktop.setAttribute(Qt.WA_TranslucentBackground)  
desktop.setAttribute(Qt.WA_NoSystemBackground)
desktop.setWindowTitle("AzuOS Desktop")

# Set the window size to something reasonable for the icons (optional)
screen = app.primaryScreen().availableGeometry()
desktop.setFixedSize(screen.width(), screen.height())

# Create layout for the grid of icons
layout = QGridLayout()
layout.setSpacing(20)  # Space between icons
layout.setContentsMargins(20, 20, 20, 20)  # Margins for top-left padding

# Load icons
icons = load_icons()

for i, app_info in enumerate(icons):
    btn = QPushButton()
    if os.path.exists(app_info["icon"]):
        btn.setIcon(QIcon(app_info["icon"]))
    else:
        btn.setText(app_info["name"])  # Fallback text if icon is not found
    
    btn.setIconSize(QSize(64, 64))
    btn.setFixedSize(100, 100)
    btn.setStyleSheet('''
        QPushButton {
            background-color: rgba(255, 255, 255, 7%);
            border: none;
            border-radius: 8px;
        }
        QPushButton:hover {
            background-color: rgba(255, 255, 255, 50%);
        }
    ''')
    btn.setToolTip(app_info["name"])
    btn.clicked.connect(lambda checked=False, cmd=app_info["exec"]: os.system(f"{cmd} &"))
    
    # Add the button to the grid layout
    layout.addWidget(btn, i // 5, i % 5)  # 5 icons per row


layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)


desktop.setLayout(layout)
desktop.lower()
# Show the desktop window
desktop.show()

sys.exit(app.exec_())
