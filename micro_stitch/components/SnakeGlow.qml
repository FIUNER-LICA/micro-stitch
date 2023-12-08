import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Layouts
import Qt5Compat.GraphicalEffects

Rectangle{
            id: snakeGlow
            
            implicitWidth: 4
            implicitHeight: 4
            border.width: 0

            radius: 5
            x: -1
            y: -1

            color: "#bcd8d9"
            property real stopX//:window.width*0.66-2*10//: parent.width
            property real stopY//: window.height-topBar.height-2*10//: parent.height
            property real initX : x
            property real initY : y
            property bool run: false
            
            // border.color: "#bcd8d9"

        SequentialAnimation{
            id: desplazar
            loops: Animation.Infinite
            running: run

            PropertyAnimation {
                target: snakeGlow
                
                property : "x"
                duration: 2000
                // running: true
                from: initX
                to: snakeGlow.stopX + x
                easing.type: Easing.Linear
                Component.onCompleted: {
            
            console.log(snakeGlow.stopX + x)}

                }
            PropertyAnimation{
                target: snakeGlow
                
                property : "y"
                duration: 2000
                from: snakeGlow.initY 
                to: snakeGlow.stopY+ snakeGlow.y
                easing.type: Easing.Linear

                // running: true
            }
            PropertyAnimation {
                target: snakeGlow
                
                property : "x"
                duration: 2000
                // running: true
                from: snakeGlow.stopX + snakeGlow.x
                to: snakeGlow.initX
                easing.type: Easing.Linear

            }
            PropertyAnimation {
                target: snakeGlow
                
                property : "y"
                duration: 2000
                // running: true
                from :snakeGlow.stopY + y
                to: initY  
                easing.type: Easing.Linear

            }
            
        }

        layer.enabled: true
        layer.effect: Glow {
            radius: 1
                            spread: 0.5
                            color: "#bcd8d9"//"#c3613c"
                            transparentBorder: true
                        }
        
}


/*##^##
Designer {
    D{i:0;height:5;width:5}
}
##^##*/
