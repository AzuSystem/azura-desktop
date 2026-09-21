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
