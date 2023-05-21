import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QWidget, QLineEdit, QSpinBox

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Calculator")
        
        # Create our Layouts
        main_layout = QHBoxLayout()

        # Create 2 columns 
        left_pane = QVBoxLayout()
        right_pane = QVBoxLayout()

        #Title label
        title_label = QLabel("VolCube Calculator")

        #Set the font
        h1_font = title_label.font()
        h1_font.setPointSize(30)
        title_label.setFont(h1_font)

        #temperature inputs
        temperature_label = QLabel("Temperature")
        temperature_spinbox= QSpinBox()
        temperature_spinbox.setMinimum(-100)
        temperature_spinbox.setMaximum(40)
        
        # Wind speed inputs
        wind_label = QLabel("Wind Speed:")
        wind_spinbox = QSpinBox()
        wind_spinbox.setMinimum(-100)
        wind_spinbox.setMaximum(40)
        

        #Results Label
        results_title = QLabel("Results")
        results_title.setAlignment(Qt.AlignmentFlag.AlignHCenter |
                                   Qt.AlignmentFlag.AlignTop)
        h2_font = results_title.font()
        h2_font.setPointSize(26)
        results_title.setFont(h2_font)
        results_window = QLineEdit("add instructions here")
        results_window.setMinimumHeight(100)

        calculate_button = QPushButton("Get Windspeed")

        #Align the label
        title_label.setAlignment(Qt.AlignmentFlag.AlignHCenter |
                                 Qt.AlignmentFlag.AlignTop)
        

        # add our left panel widgets
        left_pane.addWidget(title_label)
        left_pane.addWidget(temperature_label)
        left_pane.addWidget(temperature_spinbox)
        left_pane.addWidget(wind_label)
        left_pane.addWidget(wind_spinbox)
        left_pane.addWidget(calculate_button)

        # add our right pane widgets
        right_pane.addWidget(results_title)
        right_pane.addWidget(results_window)


        # add the two panes to the layout
        main_layout.addLayout(left_pane)
        main_layout.addLayout(right_pane)

        # set the main Layout
        gui = QWidget()
        gui.setLayout(main_layout)
        self.setCentralWidget(gui)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()