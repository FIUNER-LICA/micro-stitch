import QtQuick
import QtQuick.Controls
import Qt5Compat.GraphicalEffects

Button  {
        id: modernButton
        property url btnIconSource: "../resources/icons/minus.svg"
        property color colorDefault: "#55aaff"
        property color colorMouseOver: "#cccccc"
        property color colorPressed: "#333333"
        property int iconSize: 16
        flat: true
        highlighted: false

        QtObject {
        id: internal

        property var dynamicColor: {
            if(modernButton.down){ 
                modernButton.down ? modernButton.colorPressed: modernButton.colorDefault
                } 
            else {
                modernButton.hovered? modernButton.colorMouseOver : modernButton.colorDefault
                }
            }
        
        property bool isHover: false

        property var scaledBtn: {
            if(modernButton.hovered){ 
                modernButton.hovered ? zoomAumented.running=true: zoomAumented.running=false
                isHover = true
            } else { if(isHover){
                modernButton.hovered ? zoomDecreased.running=false: zoomDecreased.running=true
                isHover = false
            }
            }
        }
        }

        // text: qsTr("Modern Btn")
        implicitWidth: 35
        implicitHeight: 35
        // width: 35
        // height: 35

        background: Rectangle {
                    id: rec
                    color: internal.dynamicColor
                    radius: 6
                    }    

        contentItem: Item{
            Image {
                id: iconBtn
                source: modernButton.btnIconSource
                anchors.verticalCenter: parent.verticalCenter
                anchors.horizontalCenter: parent.horizontalCenter
                height: modernButton.iconSize
                width: modernButton.iconSize
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
        NumberAnimation { 
                        id: zoomAumented
                        target: modernButton
                        property : "scale"
                        from: 1
                        to: 1.05
                        duration: 200 
                        running: false // internal.scaledBtn
                                }
        NumberAnimation { 
                        id: zoomDecreased
                        target: modernButton
                        property : "scale"
                        from: 1.05
                        to: 1
                        duration: 200 
                        running: false //internal.scaledBtn
                                }
    

}


