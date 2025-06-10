import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QWidget,
                             QHBoxLayout, QLabel, QPushButton, QStackedWidget)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QColor, QLinearGradient, QPainter
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import random

class GradientWidget(QWidget):
    def paintEvent(self, event):
        painter = QPainter(self)
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0, QColor(20, 30, 50))
        gradient.setColorAt(1, QColor(10, 15, 25))
        painter.fillRect(self.rect(), gradient)

class HoneypotDashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nexus Sentinel - Advanced Honeypot System")
        self.setGeometry(100, 100, 1200, 800)

        self.main_widget = GradientWidget()
        self.setCentralWidget(self.main_widget)

        self.main_layout = QVBoxLayout(self.main_widget)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(15)

        self.create_header()

        self.content_layout = QStackedWidget()
        self.main_layout.addWidget(self.content_layout)

        self.dashboard = self.create_dashboard()
        self.threat_intel = self.create_threat_intel_view()
        self.honeypots = self.create_honeypot_config()
        self.attackers = self.create_attacker_profiles()

        self.content_layout.addWidget(self.dashboard)
        self.content_layout.addWidget(self.threat_intel)
        self.content_layout.addWidget(self.honeypots)
        self.content_layout.addWidget(self.attackers)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_dashboard)
        self.timer.start(1000)

    def create_header(self):
        header = QWidget()
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(0, 0, 0, 0)

        title = QLabel("NEXUS SENTINEL")
        title.setFont(QFont("Arial", 18, QFont.Bold))
        title.setStyleSheet("color: #00ffaa;")

        status = QLabel("ACTIVE")
        status.setFont(QFont("Arial", 12))
        status.setStyleSheet("color: #00ff00; background-color: rgba(0, 255, 0, 0.1); padding: 5px 10px; border-radius: 10px;")

        nav_buttons = QWidget()
        nav_layout = QHBoxLayout(nav_buttons)

        buttons = [
            ("Dashboard", lambda: self.content_layout.setCurrentWidget(self.dashboard)),
            ("Threat Intel", lambda: self.content_layout.setCurrentWidget(self.threat_intel)),
            ("Honeypots", lambda: self.content_layout.setCurrentWidget(self.honeypots)),
            ("Attackers", lambda: self.content_layout.setCurrentWidget(self.attackers))
        ]

        for text, action in buttons:
            btn = QPushButton(text)
            btn.setStyleSheet("""
                QPushButton {
                    color: #ffffff;
                    background-color: rgba(0, 150, 255, 0.2);
                    border: 1px solid rgba(0, 150, 255, 0.5);
                    padding: 8px 15px;
                    border-radius: 5px;
                }
                QPushButton:hover {
                    background-color: rgba(0, 150, 255, 0.4);
                }
            """)
            btn.clicked.connect(action)
            nav_layout.addWidget(btn)

        header_layout.addWidget(title)
        header_layout.addStretch()
        header_layout.addWidget(status)
        header_layout.addStretch()
        header_layout.addWidget(nav_buttons)

        self.main_layout.addWidget(header)

    def create_dashboard(self):
        dashboard = QWidget()
        layout = QVBoxLayout(dashboard)

        stats_row = QWidget()
        stats_layout = QHBoxLayout(stats_row)

        self.stat_labels = []
        stat_titles = ["Active Honeypots", "Current Attacks", "Unique IPs", "Malware Captured"]
        colors = ["#00ffaa", "#ff5555", "#55aaff", "#ffaa00"]

        for i in range(4):
            stat_widget = QWidget()
            stat_widget.setStyleSheet("background-color: rgba(30, 40, 60, 0.7); border-radius: 10px;")
            stat_layout = QVBoxLayout(stat_widget)

            title = QLabel(stat_titles[i])
            title.setStyleSheet("color: #aaaaaa; font-size: 12px;")
            stat_layout.addWidget(title)

            value = QLabel("0")
            value.setStyleSheet(f"color: {colors[i]}; font-size: 24px; font-weight: bold;")
            self.stat_labels.append(value)
            stat_layout.addWidget(value)

            stats_layout.addWidget(stat_widget)

        layout.addWidget(stats_row)

        charts_row = QWidget()
        charts_layout = QHBoxLayout(charts_row)

        self.attack_chart = FigureCanvas(Figure(figsize=(5, 3), facecolor='none'))
        self.attack_ax = self.attack_chart.figure.add_subplot(111)
        self.attack_ax.set_facecolor((0, 0, 0, 0))

        geo_widget = QWidget()
        geo_widget.setStyleSheet("background-color: rgba(30, 40, 60, 0.7); border-radius: 10px;")
        geo_label = QLabel("Geographical Attack Map\n(Would display real-time attack locations)")
        geo_label.setStyleSheet("color: white; padding: 20px;")
        geo_layout = QVBoxLayout(geo_widget)
        geo_layout.addWidget(geo_label)

        charts_layout.addWidget(self.attack_chart)
        charts_layout.addWidget(geo_widget)

        layout.addWidget(charts_row)

        return dashboard

    def create_threat_intel_view(self):
        widget = QLabel("Threat Intelligence View - Coming Soon")
        widget.setStyleSheet("color: white; font-size: 16px;")
        return widget

    def create_honeypot_config(self):
        widget = QLabel("Honeypot Configuration - Coming Soon")
        widget.setStyleSheet("color: white; font-size: 16px;")
        return widget

    def create_attacker_profiles(self):
        widget = QLabel("Attacker Profiles - Coming Soon")
        widget.setStyleSheet("color: white; font-size: 16px;")
        return widget

    def update_dashboard(self):
        data = [random.randint(5, 20), random.randint(10, 50), random.randint(5, 30), random.randint(1, 10)]
        for label, val in zip(self.stat_labels, data):
            label.setText(str(val))

        self.attack_ax.clear()
        self.attack_ax.set_facecolor((0, 0, 0, 0))
        attack_types = ['SSH', 'HTTP', 'FTP', 'RDP', 'IoT']
        attacks = [random.randint(10, 50) for _ in range(5)]
        self.attack_ax.bar(attack_types, attacks, color=['#00ffaa', '#ff5555', '#55aaff', '#ffaa00', '#aa55ff'])
        self.attack_ax.tick_params(colors='white')
        for spine in self.attack_ax.spines.values():
            spine.set_edgecolor('#444444')
        self.attack_chart.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    palette = app.palette()
    palette.setColor(palette.Window, QColor(20, 30, 50))
    palette.setColor(palette.WindowText, Qt.white)
    palette.setColor(palette.Base, QColor(30, 40, 60))
    palette.setColor(palette.AlternateBase, QColor(40, 50, 70))
    palette.setColor(palette.Text, Qt.white)
    palette.setColor(palette.Button, QColor(50, 60, 80))
    palette.setColor(palette.ButtonText, Qt.white)
    palette.setColor(palette.Highlight, QColor(0, 150, 255))
    palette.setColor(palette.HighlightedText, Qt.white)
    app.setPalette(palette)

    window = HoneypotDashboard()
    window.show()
    sys.exit(app.exec_())