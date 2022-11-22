import QtQuick 2.2

import QtQuick.Window 2.1

import QtQuick.Controls 1.2

import QtQuick.Controls.Styles 1.2

Window {

visible: true

width: 360

height: 360

MouseArea {

  anchors.fill: parent

  onClicked: {

   Qt.quit();

  }

}

ProgressBar {

  anchors.fill: parent

  anchors.margins: 40

  indeterminate: true

  style: ProgressBarStyle {

   background: Rectangle {

    radius: 2

    color: "lightgray"

    border.color: "gray"

    border.width: 1

    implicitWidth: 200

    implicitHeight: 24

   }

   progress: Rectangle {

    border.color: "steelblue"

    color: "lightsteelblue"

    // Indeterminate animation by animating alternating stripes:

    Item {

     anchors.fill: parent

     anchors.margins: 1

     visible: control.indeterminate

     clip: true

     Row {

      Repeater {

       Rectangle {

        color: index % 2 ? "steelblue" : "lightsteelblue"

        width: 20 ; height: control.height

       }

       model: control.width / 20 + 2

      }

      XAnimator on x {

       from: 0 ; to: 40

       loops: Animation.Infinite

       running: control.indeterminate

       duration: 600

      }

     }

    }

   }

  }

}

}