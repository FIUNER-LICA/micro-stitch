import QtQuick
import QtQuick.Window
import QtQuick.Controls

Window {
    width: 800
    height: 640
    visible: true
    color: "#454444"
    title: qsTr("Hello World")
    property QtObject controlers

    Rectangle {
    id: image_loc
    x: 444
    y: 409
    width: 345
    height: 222
    visible: true
    color: "#ffe4e4"
    radius: 5
    border.width: 2
Image {
    id: image
    //x: 37
    //y: 56
    //width: 100
    //height: 100
    anchors.fill: parent
    anchors.margins: 2
    asynchronous: false
    cache:false
    source: "image://myprovider/" + Math.random()
    fillMode: Image.PreserveAspectFit

}

Timer {
    id: timer_button
    interval: 10
    repeat: true
    running: false
    triggeredOnStart: true
    onTriggered: {
        image.source = "image://myprovider/" + Math.random()
    }
}
    }

Rectangle {
    id: rectangle_pano
    x: 15
    y: 22
    width: 587
    height: 381
    color: "#ebffff"
    radius: 5
    border.color: "#ffffff"
    border.width: 4

    Image {
    id: image_pano
    anchors.fill: parent
    anchors.margins: 2
    asynchronous: false
    cache:false
    source: "image://panoprovider/" + Math.random()
    fillMode: Image.PreserveAspectFit

}

Timer {
    id: timer_button_pano
    interval: 10
    repeat: true
    running: false
    triggeredOnStart: true
    onTriggered: {
        image_pano.source = "image://panoprovider/" + Math.random()
    }
}

// Connections {
//     target: controls
//     function onSend_frame() {
//         image_pano.source = "image://panoprovider/" + Math.random()
//     }
// }

}

Rectangle {
                id: boxCamType
                color: "#00000000"
                height: parent.height/12
                anchors.top: parent.top
                anchors.topMargin: parent.height/12
                anchors.right: parent.right
                anchors.rightMargin: parent.width*0.2
                anchors.left: parent.left

                ComboBox {
                    id: camType
                    anchors.left: boxCamType.left
                    anchors.right: boxCamType.right
                    baselineOffset: 0
                    rightPadding: 17
                    leftPadding: 2
                    font.italic: true
                    height: 74
                    anchors.verticalCenter: parent.verticalCenter
                    font.pointSize: 12
                    model: ["Open CV camera", "Spinnaker camera"]
                }
            }

Button {
    id: button
    x: 97
    y: 477
    width: 191
    height: 80
    text: qsTr("PLAY")
    font.italic: false
    font.bold: false
    font.pointSize: 18
    icon.color: "#adf9aa"
    // onClicked:{ panoprovider.build_panoramic_start()}
    onClicked:{ controlers.camera_selector(true, camType.currentIndex)
                timer_button.running = true
                timer_button_pano.running = true
                button.text = qsTr("Camera connected")}
}
Button {
    id: button2
    x: 97
    y: 477 + 80
    width: 191
    height: 80
    text: qsTr("STOP")
    font.italic: false
    font.bold: false
    font.pointSize: 18
    icon.color: "#adf9aa"
    onClicked:{ controlers.camera_selector(false, camType.currentIndex)
                timer_button.running = false
                timer_button_pano.running = false
                button.text = qsTr("Camera STOPPED")}
}


}



// Connections {
//                         target: plotter2
//                         function onSend(series2) {
//                             plotter2.get_series(channel2.series(0))
//                         }
//                     }
