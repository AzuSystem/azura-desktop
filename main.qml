import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.15

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
    flags: Qt.FramelessWindowHint
    color: "transparent"

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
    		model: apps

    		delegate: AppIcon {}
       	}
    }
}
