import QtQuick
import QtQuick.Controls
import Qt5Compat.GraphicalEffects


Button {
	property QtObject launcher: null

	width: 95 + 20
	height: 95 + 20

	scale: iconMouseArea.pressed ? 0.95 : 1

	property string src: "../assets/config.svg" // app icon
	property string name: "App Name"
	property string path: ""
	// property var launchr

	Behavior on scale {
		NumberAnimation {
			duration: 150
			easing.type: Easing.OutSine
		}
	}

	background: Rectangle {
		width: parent.width - 20
		height: parent.height - 20
		color: "#00ffffff"
		anchors.centerIn: parent
		radius: 8
	}

	Item {
		id: desktopIcon
		anchors.fill: parent

		// layer.enabled: true
		// layer.smooth: true
		Rectangle {
			id: desktopIconBackground
			width: parent.width - 20
			height: parent.height - 20
			color: iconMouseArea.pressed ? "#02000000" : iconMouseArea.containsMouse ? "#12ffffff" : "#01ffffff"
			border.color: iconMouseArea.pressed ? "#12ffffff" : iconMouseArea.containsMouse ? "#20ffffff" : "#12ffffff"			
			border.width: 1
			anchors.centerIn: parent
			radius: 8


			Behavior on color {
				ColorAnimation {
					duration: 50
					easing.type: Easing.InOutQuart
				}
			}

			MouseArea {
				id: iconMouseArea
				width: parent.width
				height: parent.height
				hoverEnabled: true

				onEntered: console.log(src)
				onClicked: {
					console.log(path)
					launcher.launch_item(path, "")
				}
			}
		}

		Column {
			width: parent.width
			// height: parent.height
			anchors.centerIn: parent

			Image {
				source: src
				width: 64
				height: 64
				anchors.horizontalCenter: parent.horizontalCenter
			}

			Text {
				text: name
				width: 64
				color: "#ffffff"
				anchors.horizontalCenter: parent.horizontalCenter
				horizontalAlignment: Text.AlignHCenter
				elide: Text.ElideRight
				renderType: Text.CurveRendering
			}

		}
	}
		  
	DropShadow {
		anchors.fill: desktopIcon
		source: desktopIcon
		color: "#4b000000"
		radius: 7
		samples: 64 
		horizontalOffset: 0
		verticalOffset: 2
	}
}