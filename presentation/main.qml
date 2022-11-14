import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Layouts
import Qt5Compat.GraphicalEffects
import "components"
import "resources/icons"

Window {
    id: window
    width: 1000
    height: 800
    visible: true
    color: "#00fff8f8"
    title: qsTr("Hello World")

    flags: Qt.Window | Qt.FramelessWindowHint

    //internal function

    QtObject{
        id: internal
    }
    property QtObject controlers




    Rectangle {
        id: bgHome
        color: "#454444"
        radius: 0
        border.width: 0
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: topBar.bottom
        anchors.bottom: parent.bottom
        anchors.topMargin: 0

        // AnimatedImage {
        //     id: animatedImage
        //     opacity: 0.6
        //     anchors.fill: parent
        //     anchors.bottom: parent.bottom
        //     source: "resources/Cell-Division-Animation-goback.gif"
        //     anchors.rightMargin: 5
        //     anchors.leftMargin: 5
        //     anchors.bottomMargin: 5
        //     anchors.topMargin: 5
        //     clip: true
        //     cache: true
        //     autoTransform: true
        //     asynchronous: false
        // }

        Rectangle {
            id: rectangle_pano
            x: 10
            y: 10
            color: "#00ebffff"
            radius: 6
            border.color: "#bcd8d9"
            border.width: 4
            anchors.left: parent.left
            anchors.right: appControls.left
            anchors.top: parent.top
            anchors.bottom: parent.bottom
            anchors.leftMargin: 10
            anchors.topMargin: 10
            anchors.bottomMargin: 10
            anchors.rightMargin: 10



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
            layer.enabled: true
            layer.effect: Glow {
        // id: glow
        // anchors.left: rectangle_pano.right
        // anchors.right: rectangle_pano.left
        // anchors.top: rectangle_pano.top
        // anchors.bottom: rectangle_pano.bottom
        // anchors.rightMargin: 1
        // anchors.leftMargin: 1
        // anchors.bottomMargin: 1
        // anchors.topMargin: 1
        // opacity: 0.65
        radius: 8
        // samples: 17
        spread: 0.5
        color: "#bcd8E5"
        transparentBorder: true
        // source: rectangle_pano
    }
        }

        Image {
                id: image_pano
                anchors.fill: rectangle_pano
                anchors.margins: 10
                asynchronous: false
                cache:false
                source: "image://panoprovider/" + Math.random()
                fillMode: Image.PreserveAspectFit

            }

        Rectangle {
            id: appControls
            x: 660
            y: 10
            color: "#0058fc74"
            radius: 6
            border.color: "#bcd8d9"
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
                color: "#00ffe4e4"
                radius: 6
                border.color: "#bcd8d9"
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

            Rectangle {
                id: videoControls
                color: "#ffffff"
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: boxCamType.bottom
                anchors.bottom: parent.bottom
                anchors.topMargin: 10
                anchors.bottomMargin: parent.height*0.15
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

                RowLayout {
                    id: playStopBtns
                    anchors.left: parent.left
                    anchors.right: parent.right
                    anchors.top: controlsTitle.bottom
                    anchors.bottom: parent.bottom
                    anchors.topMargin: 10
                    anchors.rightMargin: 4
                    anchors.leftMargin: 4
                    anchors.bottomMargin: 4
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
                anchors.topMargin: 10
                anchors.rightMargin: 4
                anchors.leftMargin: 4
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

    Rectangle {
        id: topBar
        height: 60
        color: "#454444"
        radius: 0
        border.width: 0
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: parent.top
        gradient: Gradient {
            GradientStop {
                position: 0.60274
                color: "#434343"
            }

            GradientStop {
                position: 0
                color: "#1c1c1c"
            }

            orientation: Gradient.Vertical
            GradientStop {
                position: 0.10502
                color: "#2b2b2b"
            }
        }
        anchors.rightMargin: 0
        anchors.leftMargin: 0
        anchors.topMargin: 0

        Rectangle {
            id: titleBar
            height: 35
            color: "#0029323c"
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: parent.top
            anchors.rightMargin: 35*3
            anchors.leftMargin: 0
            anchors.topMargin: 0
            DragHandler {
                onActiveChanged: if (active){
                    window.startSystemMove()
                }
            }

            Image {
                id: iconApp
                width: 28
                anchors.left: parent.left
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                source: "qrc:/qtquickplugin/images/template_image.png"
                anchors.topMargin: 0
                anchors.bottomMargin: 0
                anchors.leftMargin: 5
                fillMode: Image.PreserveAspectFit
            }

            Text {
                id: titleApp
                color: "#bcd8d9"
                text: qsTr("Micros Stitch")
                anchors.left: iconApp.right
                anchors.right: parent.right
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                font.pixelSize: 16
                horizontalAlignment: Text.AlignLeft
                verticalAlignment: Text.AlignVCenter
                font.bold: false
                font.italic: false
                anchors.leftMargin: 5
            }
        }

        Rectangle {
            id: topBarDescription
            height: 25
            color: "#454444"
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: titleBar.bottom
            anchors.leftMargin: 0
            anchors.rightMargin: 0
            anchors.topMargin: 0

            Label {
                id: labelLeftInfo
                color: "#84a5a6"
                text: qsTr("Stitching in real-time a panoramic image of microscopy")
                anchors.fill: parent
                verticalAlignment: Text.AlignVCenter
                font.pointSize: 10
                anchors.rightMargin: 300
                anchors.leftMargin: 10
            }

            Label {
                id: labelRightInfo
                color: "#84a5a6"
                text: qsTr("| HOME")
                anchors.left: labelLeftInfo.right
                anchors.right: parent.right
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                horizontalAlignment: Text.AlignRight
                verticalAlignment: Text.AlignVCenter
                anchors.rightMargin: 10
                anchors.leftMargin: 0
                font.pointSize: 10
            }
        }

        Row {
            id: topBarButtons
            height: 35
            anchors.left: titleBar.right
            anchors.right: parent.right
            anchors.top: parent.top
            anchors.topMargin: 0
            anchors.rightMargin: 0
            anchors.leftMargin: 0
            TopBarButton{ id: minimized
            onClicked: window.showMinimized()
            }

            TopBarButton {
                id: maximize
                btnIconSource: "../resources/icons/square.svg"
                iconSize: 13
                onClicked: window.showMaximized()

            }

            TopBarButton {
                id: exit
                btnIconSource: "../resources/icons/x.svg"
                onClicked: window.Close()
            }
        }
    }

}

