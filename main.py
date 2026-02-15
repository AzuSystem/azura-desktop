import sys
import os
import subprocess
import shlex
from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5.QtGui import QGuiApplication, QIcon
from PyQt5.QtQml import QQmlApplicationEngine

if not os.path.exists("/tmp/azura-desktop-area-icon-previews"):
	print('"/tmp/azura-desktop-area-icon-previews" Created ( Required for Icon Previews )')
	os.makedirs("/tmp/azura-desktop-area-icon-previews", exist_ok=True)

app = QGuiApplication(sys.argv)

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
			for line in content:
				if line.startswith('Name='):
					name = line.strip().split('=')[1]
				elif line.startswith('Icon='):
					icon = line.strip().split('=')[1]


			if name:
				# it's time i cook up some dodgy black magic for theme matching icons :sob:
				pixmap = QIcon.fromTheme(icon, QIcon("assets/config.svg")).pixmap(64, 64)
				pixmap.save("/tmp/azura-desktop-area-icon-previews/" + icon + ".png")
				# pixmap.save("/tmp/azura-desktop-area-icon-previews/" + icon + ".jpg")
				pixmap.save("/tmp/azura-desktop-area-icon-previews/" + icon + ".svg")

				# fallback icon
				icon_path = icon if icon else "/usr/share/icons/hicolor/128x128/apps/default-icon.png"
				icons.append({
					"name": name,
					"type": "app",
					# "src": "file://" + icon_path,
					# "src": QIcon.fromTheme(icon_path, QIcon("assets/config.svg")),
					"icon": "/tmp/azura-desktop-area-icon-previews/" + icon_path,
					"path": file_path
				})
		else:
			icons.append({
				"name": filename,
				"type": "unknown",
				"icon": "assets/config.svg",
				"icon": file_path
			})

	return icons

print(fetch_desktop())

class Launcher(QObject):
	@pyqtSlot(str, str) # (command, type) parametersss yeaaa
	def launch_item(self, command, type=""):
		# for placeholder in ["%U", "%F", "%i", "%c", "%k"]: # weird stuff in .desktop files, i should probably learn them-
		# 	command = command.replace(placeholder, "")
		# 	print(command)
		# args = shlex.split(command)
		# subprocess.Popen(args, start_new_session=True)

		subprocess.Popen(["dex", command], start_new_session=True)

		print(command)

engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)

model = fetch_desktop()

launcher = Launcher()
engine.rootContext().setContextProperty("launcher", launcher)
engine.rootContext().setContextProperty("apps", model)

engine.load('main.qml')

root = engine.rootObjects()[0]
# root.setProperty("launcher", launcher)


sys.exit(app.exec())