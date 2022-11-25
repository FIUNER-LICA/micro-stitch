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
    height: 700
    visible: true
    color: "#00fff8f8"
    title: qsTr("Stitching Aplication")

    flags: Qt.Window | Qt.FramelessWindowHint

    // Properties
    property int windowStatus : 0

    //internal function

    QtObject{
        id: internal

        function maximizeRestore(){
            if (windowStatus==0){
                windowStatus = 1
                btnMaximize.btnIconSource = "../resources/icons/icon_restore.png"
                btnMaximize.iconSize =  20
                window.showMaximized()
            }
            else{
                windowStatus = 0
                btnMaximize.btnIconSource = "../resources/icons/square.svg"
                btnMaximize.iconSize =  13
                window.showNormal()
            }
        }
        function ifMaximizedWindowsRestore(){
            if (windowStatus == 1){
                // window.showNormal()
                windowStatus = 0
                btnMaximize.btnIconSource = "../resources/icons/square.svg"
                btnMaximize.iconSize =  13
            }
        }
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

        Rectangle {
            id: rectangle_pano
            color: "#00ebffff"
            radius: 6
            border.color: "#bcd8d9"
            border.width: 2
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

            layer.enabled: true
            layer.effect: Glow {
                id: glowRectPano
                radius: 6
                spread: 0.5
                color: "#bcd8E5"
                transparentBorder: true
            }

            SnakeGlow{
                id: sng
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
            color: "#0058fc74"
            radius: 6
            border.color: "#bcd8d9"
            border.width: 0
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
                height: parent.height*0.45
                visible: true
                color: "#00ffe4e4"
                radius: 6
                border.color: "#bcd8d9"
                border.width: 2
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: parent.top
                anchors.topMargin: 0
                anchors.rightMargin: 0
                anchors.leftMargin: 0
                
                RectangleGlowEffect{}

                Image {
                    id: image

                    anchors.fill: parent
                    anchors.margins: 2
                    asynchronous: false

                    source: "image://myprovider/" + Math.random()
                    anchors.rightMargin: 10
                    anchors.leftMargin: 10
                    anchors.bottomMargin: 10
                    anchors.topMargin: 10
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
                id: controlsRect
                color: "#00ffffff"
                radius: 6
                border.color: "#bcd8d9"
                border.width: 2
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: image_loc.bottom
                anchors.bottom: parent.bottom
                anchors.bottomMargin: 0
                anchors.rightMargin: 0
                anchors.leftMargin: 0
                anchors.topMargin: 10

                RectangleGlowEffect {
                }

                Text {
                    id: camTypeTitle
                    x: 10
                    y: 0
                    color: "#bcd8d9"
                    text: qsTr("Camera type")
                    anchors.left: parent.left
                    anchors.right: parent.right
                    anchors.top: parent.top
                    font.pixelSize: 16
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    anchors.topMargin: 15
                    font.italic: false
                    font.bold: true
                    anchors.rightMargin: 10
                    anchors.leftMargin: 10
                }

                Rectangle {
                    id: boxCamType
                    height: 45
                    color: "#00000000"
                    radius: 6
                    border.width: 0
                    anchors.left: parent.left
                    anchors.right: parent.right
                    anchors.top: camTypeTitle.bottom
                    anchors.topMargin: 10
                    anchors.rightMargin: 6
                    anchors.leftMargin: 6
                    
                    ComboBox {
                        id: camType
                        anchors.fill: parent
                        layer.wrapMode: ShaderEffectSource.ClampToEdge
                        layer.enabled: true
                        layer.textureMirroring: ShaderEffectSource.NoMirroring
                        baselineOffset: 0
                        font.weight: Font.Normal
                        anchors.rightMargin: 6
                        anchors.bottomMargin: 4
                        anchors.leftMargin: 6
                        anchors.topMargin: 6
                        font.hintingPreference: Font.PreferVerticalHinting
                        antialiasing: true
                        activeFocusOnTab: false
                        focusPolicy: Qt.StrongFocus
                        spacing: 2
                        rightPadding: 17
                        leftPadding: 2
                        
                        font.italic: true
                        font.pointSize: 12
                        flat: true
                        model: ["Spinnaker camera", "Open CV camera"]
                        delegate: ItemDelegate {
                            width: camType.width
                            contentItem: Text {
                                id: textModelData
                                text: modelData
                                color: "#bcd8d9"
                                font: camType.font
                                elide: Text.ElideRight
                                verticalAlignment: Text.AlignVCenter
                                horizontalAlignment: Text.AlignHCenter
                            }
                            highlighted: camType.highlightedIndex === index
                            background: Rectangle {
                                    radius: 6
                                    color: "transparent"//"#bcd8d9"
                                    // width: camType.width-40
                                    anchors {left: parent.left; right:parent.right}
                                }
                        }
                        indicator: Canvas {
                            id: canvas
                            x: camType.width - width - camType.rightPadding
                            y: camType.topPadding + (camType.availableHeight - height) / 2
                            width: 14
                            height: 10
                            contextType: "2d"
                            
                            Connections {
                                target: camType
                                function onPressedChanged() { canvas.requestPaint(); }
                            }

                            onPaint: {
                                context.reset();
                                context.moveTo(0, 0);
                                context.lineTo(width, 0);
                                context.lineTo(width / 2, height);
                                context.closePath();
                                context.fillStyle = camType.pressed ? "#768f90":"#bcd8d9";
                                context.fill();
                            }
                        }

                        contentItem: Text {
                            leftPadding: 0
                            rightPadding: camType.indicator.width + camType.spacing
                            text: camType.displayText
                            font: camType.font
                            color: camType.pressed ? "#768f90": "#bcd8d9"//"#17a81a" : "#21be2b"
                            verticalAlignment: Text.AlignVCenter
                            horizontalAlignment: Text.AlignHCenter
                            elide: Text.ElideRight
                        }                         
                        
                        popup: Popup {
                            y: camType.height - 1
                            width: camType.width
                            implicitHeight: contentItem.implicitHeight
                            padding: 4
                            
                            contentItem: ListView {
                                id: listView
                                clip: true
                                focus: true
                                implicitHeight: contentHeight
                                implicitWidth: contentWidth
                                model: camType.popup.visible ? camType.delegateModel : null
                                delegate: camType.delegate
                                currentIndex: camType.highlightedIndex
                                highlight: Rectangle {
                                    z:2
                                    color: "#86bcd8d9"
                                    // anchors { left: camType.left; right:camType.right}
                                    radius: 6
                                }
                                ScrollIndicator.vertical: ScrollIndicator {}
                            }
                            

                            background: Rectangle {
                                color: "#454444" 
                                border.color: "#bcd8d9"
                                border.width: 2
                                radius: 6
                            }
                        }

                        background: Rectangle {    
                            color:"#00ffffff"
                            radius: 6
                            border.color: "#bcd8d9"//camType.pressed ? "#17a81a" : "#21be2b"
                            border.width: camType.popup.visible ?  3 : 2
                        }

                        RectangleGlowEffect{}
                    }
                }

                Rectangle {
                    id: videoControls
                    x: 4
                    y: 87
                    height: 130
                    color: "#00ffffff"
                    border.width: 0
                    anchors.left: parent.left
                    anchors.right: parent.right
                    anchors.top: boxCamType.bottom
                    anchors.topMargin: 10
                    anchors.rightMargin: 6
                    anchors.leftMargin: 6

                    Text {
                        id: controlsTitle
                        color: "#bcd8d9"
                        text: qsTr("Controllers")
                        anchors.left: parent.left
                        anchors.right: parent.right
                        anchors.top: parent.top
                        font.pixelSize: 16
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                        font.italic: false
                        font.bold: true
                        anchors.rightMargin: 4
                        anchors.leftMargin: 4
                        anchors.topMargin: 3
                    }

                    RowLayout {
                        id: playStopBtns
                        anchors.left: parent.left
                        anchors.right: parent.right
                        anchors.top: controlsTitle.bottom
                        antialiasing: true
                        anchors.rightMargin: 6
                        anchors.leftMargin: 6
                        clip: false
                        layoutDirection: Qt.LeftToRight
                        anchors.topMargin: 16
                        spacing: 15

                        Rectangle {
                            id: playVideoBtn
                            width: parent.width*0.45
                            height: 80
                            color: "#00ffffff"
                            radius: 6
                            border.width: 0
                            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                            Layout.minimumWidth: parent.width*0.4
                            Layout.preferredWidth: parent.width*0.4
                            z: 1
                            Layout.leftMargin: 4
                            Layout.rightMargin: 0
                            // text: qsTr("PLAY")
                            // flat: false
                            Layout.fillHeight: true
                            // font.italic: false
                            // font.bold: false
                            // font.pointSize: 18
                            // icon.color: "#adf9aa"
                            // onClicked:{ panoprovider.build_panoramic_start()}
                            ControlsButton{
                                anchors.fill: parent
                                colorMouseOver: "#86bcd8d9"
                                iconSize: 33
                                btnIconSource: "../resources/icons/play.svg"
                                colorDefault: "#0055aaff"
                                RectangleGlowEffect{}
                            onClicked:{ controlers.camera_selector(true, camType.currentIndex)
                                timer_button.running = true
                                // timer_button_pano.running = true
                                }
                            
                            }
                        }

                        Rectangle {
                            id: stopVideoBtn
                            width: parent.width*0.45
                            color: "#00ffffff"
                            radius: 6
                            border.width: 0
                            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                            transformOrigin: Item.Center
                            Layout.minimumWidth: parent.width*0.4
                            Layout.preferredWidth: parent.width*0.4
                            z: 1
                            Layout.rightMargin: 4
                            // width: 191
                            // height: 80
                            // text: qsTr("STOP")
                            Layout.fillHeight: true
                            // font.italic: false
                            // font.bold: false
                            // font.pointSize: 18
                            // icon.color: "#adf9aa"
                            ControlsButton{
                                anchors.fill: parent
                                iconSize: 30
                                colorDefault: "#0055aaff"
                                btnIconSource: "../resources/icons/square.svg"
                                colorMouseOver: "#86bcd8d9"
                                RectangleGlowEffect{}
                            onClicked:{ controlers.camera_selector(false, camType.currentIndex)
                                timer_button.running = false
                                timer_button_pano.running = false
                                // playVideoBtn.text = qsTr("Camera STOPPED")}
                                }
                            }
                            
                        }
                    }
                }

                Rectangle {
                    id: saveArea
                    x: 4
                    y: 248
                    color: "#00ffffff"
                    border.width: 0
                    anchors.left: parent.left
                    anchors.right: parent.right
                    anchors.top: videoControls.bottom
                    anchors.bottom: parent.bottom
                    anchors.topMargin: 15
                    anchors.rightMargin: 10
                    anchors.leftMargin: 10
                    anchors.bottomMargin: 10

                    ControlsButton{ 
                        id: btnSave
                        anchors.fill: parent
                        iconSize: parent.height*0.42
                        colorMouseOver: "#86bcd8d9"
                        colorDefault: "#00bcd8d9"
                        btnIconSource: "../resources/icons/save.svg"
                        RectangleGlowEffect{}
                        onClicked:{ controlers.panoramic_init(true)
                                // timer_button.running = true
                                timer_button_pano.running = true
                                }
                    }
                    

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
                                     internal.ifMaximizedWindowsRestore()
                                 }
            }

            Image {
                id: iconApp
                width: 28
                anchors.left: parent.left
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                // source: "resources/images/logo.png"
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
            
                onClicked: {window.showMinimized()
                    sng.run = false
                }
            }

            TopBarButton {
                id: btnMaximize
                btnIconSource: "../resources/icons/square.svg"
                iconSize: 13
                onClicked: {internal.maximizeRestore()
                    sng.stopX = window.width*0.66-(2*10+1)
                    sng.stopY = window.height-topBarDescription.height-titleBar.height-2*10-1
                    sng.run = true
                }


            }

            TopBarButton {
                id: exit
                btnColorMouseOver: "#b30000"
                btnColorClicked: "#a11b40"
                btnIconSource: "../resources/icons/x.svg"
                onClicked: Qt.quit()
            }
        }
    }

}


/*##^##
Designer {
    D{i:0;formeditorZoom:0.9;height:700;width:1000}
}
##^##*/
