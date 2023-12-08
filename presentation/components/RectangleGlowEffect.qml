import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import Qt5Compat.GraphicalEffects


Rectangle {
                id: rectGlowEffect
                color: "#00ffffff"
                radius: 6
                border.color: "#bcd8d9"
                border.width: 1
                anchors.fill: parent
                layer.enabled: true
                layer.effect: Glow {
                    id: glowControls
                    radius: 6
                    spread: 0.5
                    color: "#bcd8E5"
                    transparentBorder: true
                }
            }