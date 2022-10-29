import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Layouts

Window {
    id: window
    width: 1000
    height: 800
    visible: true
    color: "#454444"
    title: qsTr("Hello World")
    property QtObject controlers

    Rectangle {
        id: rectangle_pano
        color: "#ebffff"
        radius: 5
        border.color: "#ffffff"
        border.width: 4
        anchors.left: parent.left
        anchors.right: appControls.left
        anchors.top: parent.top
        anchors.bottom: parent.bottom
        anchors.leftMargin: 10
        anchors.topMargin: 10
        anchors.bottomMargin: 10
        anchors.rightMargin: 10

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
        id: appControls
        color: "#4b58fc74"
        radius: 10
        border.color: "#df4eff5f"
        border.width: 2
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.bottom: parent.bottom
        anchors.topMargin: 10
        anchors.leftMargin: parent.width*0.66
        anchors.bottomMargin: 10
        anchors.rightMargin: 10

        Rectangle {
            id: image_loc
            height: 222
            visible: true
            color: "#ffe4e4"
            radius: 5
            border.width: 2
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: parent.top
            anchors.topMargin: 10
            anchors.rightMargin: 4
            anchors.leftMargin: 4
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

        Text {
            id: camTypeTitle
            text: qsTr("Tipo de cámara")
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: image_loc.bottom
            font.pixelSize: 16
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            font.italic: false
            font.bold: true
            anchors.rightMargin: 4
            anchors.leftMargin: 4
            anchors.topMargin: parent.height*0.01
        }

        Rectangle {
            id: boxCamType
            color: "#00000000"
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: camTypeTitle.bottom
            anchors.bottom: parent.bottom
            anchors.bottomMargin: parent.height*0.55
            anchors.topMargin: parent.height*0.01
            anchors.rightMargin: 4
            anchors.leftMargin: 4

            ComboBox {
                id: camType
                anchors.fill: parent
                anchors.rightMargin: 4
                anchors.leftMargin: 4
                anchors.bottomMargin: 4
                anchors.topMargin: 4
                baselineOffset: 0
                rightPadding: 17
                leftPadding: 2
                font.italic: true
                font.pointSize: 12
                model: ["Open CV camera", "Spinnaker camera"]
            }
        }

        Slider {
            id: focusSlider
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: focusTitle.bottom
            anchors.bottom: parent.bottom
            enabled: true
            live: false
            to: 100
            anchors.bottomMargin: parent.height*0.47
            anchors.topMargin: parent.height*0.01
            touchDragThreshold: 0
            stepSize: 100
            anchors.rightMargin: 4
            anchors.leftMargin: 4
            value: 0
        }

        Text {
            id: focusTitle
            text: qsTr("Foco")
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: boxCamType.bottom
            font.pixelSize: 16
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            font.bold: true
            anchors.rightMargin: 4
            anchors.leftMargin: 4
            anchors.topMargin: parent.height*0.01
        }

        Rectangle {
            id: videoControls
            color: "#ffffff"
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: focusSlider.bottom
            anchors.bottom: parent.bottom
            anchors.bottomMargin: parent.height*0.15
            anchors.topMargin: parent.height*0.01
            anchors.rightMargin: 4
            anchors.leftMargin: 4

            Text {
                id: controlsTitle
                text: qsTr("Controles")
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                font.pixelSize: 16
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.bottomMargin: parent.height*0.8
                font.bold: false
                anchors.rightMargin: 4
                anchors.leftMargin: 4
                anchors.topMargin: 4
            }

            Column {
                id: monoRGBselect
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: controlsTitle.bottom
                anchors.bottom: parent.bottom
                spacing: 2
                z: 2
                focus: true
                anchors.bottomMargin: parent.height*0.50
                anchors.rightMargin: 4
                anchors.leftMargin: 4
                anchors.topMargin: appControls.height*0.01

                RadioButton {
                    id: videoRGB
                    text: qsTr("Video RGB")
                    anchors.left: parent.left
                    anchors.right: parent.right
                    anchors.top: parent.top
                    anchors.bottom: parent.verticalCenter
                    anchors.leftMargin: 0
                    anchors.rightMargin: 0
                    anchors.bottomMargin: 0

                    checked: true
                    
                    contentItem: Text {
                        text: videoRGB.text
                        anchors.fill: parent
                        color: "#518c89"
                        leftPadding: videoRGB.indicator.width + videoRGB.spacing
                        verticalAlignment: Text.AlignVCenter
                        font.pointSize: 14
                    }
                }

                RadioButton {
                    id: videoMono
                    text: qsTr("Video monocromático")
                    anchors.left: parent.left
                    anchors.right: parent.right
                    anchors.top: parent.verticalCenter
                    anchors.bottom: parent.bottom
                    anchors.topMargin: 0
                    contentItem: Text {
                        text: eventDownload.text
                        color: "#518c89"
                        leftPadding: videoMono.indicator.width + videoMono.spacing
                        verticalAlignment: Text.AlignVCenter
                        font.pointSize: 14
                    }
                    onClicked: {}
                }
            }

            RowLayout {
                id: playStopBtns
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: monoRGBselect.bottom
                anchors.bottom: parent.bottom
                anchors.rightMargin: 4
                anchors.leftMargin: 4
                anchors.bottomMargin: 4
                anchors.topMargin: appControls.height*0.01
                layer.samples: 2
                z: 2
                spacing: 10

                Button {
                    id: playVideoBtn
                    width: 191
                    height: 80
                    text: qsTr("PLAY")
                    Layout.fillHeight: true
                    Layout.fillWidth: true
                    Layout.preferredWidth: parent.width*0.4
                    font.italic: false
                    font.bold: false
                    font.pointSize: 18
                    icon.color: "#adf9aa"
                    // onClicked:{ panoprovider.build_panoramic_start()}
                    onClicked:{ controlers.camera_selector(true, camType.currentIndex)
                        timer_button.running = true
                        timer_button_pano.running = true
                        playVideoBtn.text = qsTr("Camera connected")}
                }

                Button {
                    id: stopVideoBtn
                    width: 191
                    height: 80
                    text: qsTr("STOP")
                    Layout.fillHeight: true
                    Layout.fillWidth: true
                    Layout.preferredWidth: parent.width*0.40
                    Layout.alignment: Qt.AlignRight | Qt.AlignVCenter
                    font.italic: false
                    font.bold: false
                    font.pointSize: 18
                    icon.color: "#adf9aa"
                    onClicked:{ controlers.camera_selector(false, camType.currentIndex)
                        timer_button.running = false
                        timer_button_pano.running = false
                        playVideoBtn.text = qsTr("Camera STOPPED")}
                }
            }



        }

        Rectangle {
            id: saveArea
            color: "#ffffff"
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: videoControls.bottom
            anchors.bottom: parent.bottom
            anchors.rightMargin: 4
            anchors.leftMargin: 4
            anchors.topMargin: parent.height*0.01
            anchors.bottomMargin: 10

            Button {
                id: button
                text: qsTr("GUARDAR")
                anchors.fill: parent
                font.italic: true
                font.bold: false
                font.pointSize: 16
                anchors.rightMargin: 4
                anchors.leftMargin: 4
                anchors.bottomMargin: 4
                anchors.topMargin: 4
            }
        }
    }


}



// Connections {
//                         target: plotter2
//                         function onSend(series2) {
//                             plotter2.get_series(channel2.series(0))
//                         }
//                     }

/*##^##
Designer {
    D{i:0;formeditorZoom:0.75}D{i:1}D{i:5}D{i:8}D{i:10}D{i:9}D{i:11}D{i:12}D{i:14}D{i:20}
D{i:13}D{i:24}D{i:23}D{i:4}
}
##^##*/
