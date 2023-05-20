import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QVBoxLayout, QLabel

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Calculator")
        
        main_layout = QHBoxLayout()

        left_pane = QVBoxLayout()
        right_pane = QVBoxLayout()

        #Title label
        title_label = QLabel("VolCube Calculator")

        #Set the font
        h1_font = title_label.font()
        h1_font.setPointSize(30)
        title_label.setFont(h1_font)

        #Results Label
        results_label = QLabel("Results")
        h2_font = results_label.font()
        h2_font.setPointSize(26)
        results_label.setFont(h2_font)

        title_label.setAlignment(Qt.AlignmentFlag.AlignHCenter |
                                 Qt.AlignmentFlag.AlignTop)
        
        self.setFixedSize(QSize(400, 300))

        left_pane.addWidget(title_label)

        right_pane.addWidget(results_label)

        main_layout.addLayout(left_pane)
        main_layout.addLayout(right_pane)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()