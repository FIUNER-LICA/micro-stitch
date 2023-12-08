import QtQuick
import QtQuick.Controls
import Qt5Compat.GraphicalEffects

Button {
    id: toggleBtn
    property alias toggleBtnIconsource: toggleBtn.icon.source
    property url btnIconSource: "../resources/icons/arrow-up.svg"
    property color btnColorDefault: "#a6039b"
    property color btnColorMouseOver: "#d989cb"
    property color btnColorClicked: "#8c0375"

    QtObject {
        id: internal
        //Mouse over and click change color
        property var dynamicColor: if (toggleBtn.down){
                                   toggleBtn.down ? toggleBtn.btnColorClicked : toggleBtn.btnColorDefault
                                   } else {
                                   toggleBtn.hovered ? toggleBtn.btnColorMouseOver : toggleBtn.btnColorDefault
                                   }
    }

    implicitWidth: 35
    implicitHeight: 30

    background: Rectangle {
    id: bgBtn
    color:"#00a6039b" //internal.dynamicColor
    radius: 5

    Image {
    id: iconBtn
    source: toggleBtn.btnIconSource
    anchors.verticalCenter: parent.verticalCenter
    anchors.horizontalCenter: parent.horizontalCenter
    height: 35
    width: 30
    fillMode: Image.PreserveAspectFit
    antialiasing: false
    }
    ColorOverlay {
    anchors.fill: iconBtn
    source: iconBtn
    color: internal.dynamicColor
    //color: "#a6039b"
    antialiasing: false
    }
  }
}
