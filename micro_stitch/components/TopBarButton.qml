import QtQuick
import QtQuick.Controls
import Qt5Compat.GraphicalEffects

Button {
    id: btnTopBar
    // property alias toggleBtnIconsource: btnTopBar.icon.source
    property url btnIconSource: "../resources/icons/minus.svg"
    property color btnColorDefault:  "#0029323c"//"#1c1d20"

    property color btnColorMouseOver: "#23272E"
    property color btnColorClicked: "#00a1f1"

    property int iconSize: 16
	// highlighted: true
	flat: true
	
    QtObject {
        id: internal
        //Mouse over and click change color
        property var dynamicColor: if (btnTopBar.down){
                                   btnTopBar.down ? btnColorClicked : btnColorDefault
                                   } else {
                                   btnTopBar.hovered ? btnColorMouseOver : btnColorDefault
                                   }
    }

    // implicitWidth: 35
    // implicitHeight: 35
    width: 35
    height: 35
	

    background: Rectangle {
					id: bgBtn
					color: internal.dynamicColor
    }
    contentItem: Item{
    Image {
    id: iconBtn
    source: btnIconSource
    anchors.verticalCenter: parent.verticalCenter
    anchors.horizontalCenter: parent.horizontalCenter
    height: iconSize
    width: iconSize
    visible: false
    fillMode: Image.PreserveAspectFit
    antialiasing: false
    }
    ColorOverlay {
    anchors.fill: iconBtn
    source: iconBtn
    color: "#bcd8d9"
    antialiasing: false
    }


  }
}

/*##^##
Designer {
    D{i:0;height:35;width:35}
}
##^##*/
