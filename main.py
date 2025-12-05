import sys
import os
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine

# ~/Desktop
def fetch_desktop():
    desktop_path = os.path.expanduser('~/Desktop')

    if not os.path.exists(desktop_path):
        return []

    icons = []

    for filename in os.listdir(desktop_path):
        file_path = os.path.join(desktop_path, filename)

        # filter out .desktop specfically
        if filename.endswith('.desktop'):
            with open(file_path, 'r') as f:
                content = f.readlines()
            
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

            if name and exec_cmd:
            	# fallback icon
                icon_path = icon if icon else "/usr/share/icons/hicolor/128x128/apps/default-icon.png"
                icons.append({
                    "name": name,
                    "src": icon_path,
                    "exec": exec_cmd
                })
        else:
            icons.append({
                "name": filename,
                "src": "assets/config.svg",
                "exec": ""
            })

    return icons

print(fetch_desktop())

app = QGuiApplication(sys.argv)

engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)

model = fetch_desktop()
engine.rootContext().setContextProperty("apps", model)

engine.load('main.qml')

root = engine.rootObjects()[0]

sys.exit(app.exec())