import QtQuick
import QtQuick.Controls
import QtQuick.Window
import com.azusystem.azura

Window {
	id: window
	title: "Azura Desktop"
	visible: true
	width: screen.width
	height: screen.height
	minimumWidth: width
    maximumWidth: width
    minimumHeight: height
    maximumHeight: height
    // flags: Qt.FramelessWindowHint
    flags: Qt.FramelessWindowHint | Qt.WindowStaysOnBottomHint
    // flags: Qt.FramelessWindowHint | Qt.X11BypassWindowManagerHint | Qt.WindowStaysOnBottomHint
    color: "transparent"

    property var launcherClass: launcher // ive been stuck for 3 WHOLE HOURS trying to get this into AppIcon.qml, this was the fix?????

	DesktopList {
		id: desktopList
	}

    Rectangle {
    	width: parent.width - 20
    	height: parent.height - 20
    	color: "#00ffffff"
    	anchors.centerIn: parent

		// ListModel {
		// 	id: apps
    	// 	ListElement { name: "App Name" }
    	// 	ListElement { name: "App Name" }
    	// 	ListElement { name: "App Name" }
    	// 	ListElement { name: "App Name" }
    	// 	ListElement { name: "App Name" }
    	// }

    	GridView {
    		anchors.fill: parent
    		cellWidth: 95 + 20
    		cellHeight: 95 + 20
    		model: JSON.parse(desktopList.fetchDesktop())
    		interactive: false
    		keyNavigationEnabled: true
    		// model: launcher.launch_item("vlc", "")

    		delegate: AppIcon {
    			// launcher: launcher
    			launcher: window.launcherClass // weird workaround i think, to get launcher function in the element 
    			name: modelData.name
    			src: modelData.icon // src is the app icon
    			path: modelData.path
    		}
       	}
    }

	Component.onCompleted: {
		console.log(desktopList.fetchDesktop())
		// const apps = JSON.parse(desktopList.fetchDesktop())
	}
}
