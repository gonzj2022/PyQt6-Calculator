import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QWidget, QTextEdit, QSpinBox
from PyQt6.QtGui import QIcon, QPixmap
import controller

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Calculator")
        
        #App Icon
        self.icon = "Images/cube.png"
        self.setWindowIcon(QIcon(self.icon))
        
        #Cube Image
        label = QLabel(self)
        pixmap = QPixmap("Images/Gray Cube.png")
        label.setPixmap(pixmap)

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

        # Cube Length inputs
        Length_label = QLabel("Length")
        self.Length_Spinbox = QSpinBox()
        self.Length_Spinbox.setMinimum(0)
        
        #Cube Width inputs
        Width_label = QLabel("Width")
        self.Width_Spinbox = QSpinBox()
        self.Width_Spinbox.setMinimum(0)

        #Cube Height inputs
        Height_label = QLabel("Height")
        self.Height_Spinbox = QSpinBox()
        self.Height_Spinbox.setMinimum(0)

        #Results Label
        results_title = QLabel("Volume")
        results_title.setAlignment(Qt.AlignmentFlag.AlignHCenter |
                                   Qt.AlignmentFlag.AlignTop)
        h2_font = results_title.font()
        h2_font.setPointSize(24)
        results_title.setFont(h2_font)
        self.results_window = QLabel("Results appear here")
        self.results_window.setMinimumHeight(100)

        self.calculate_button = QPushButton("Calculate")
        # add a calculate function
        self.calculate_button.clicked.connect(self.calculate_volume)


        #Align the label
        title_label.setAlignment(Qt.AlignmentFlag.AlignHCenter |
                                 Qt.AlignmentFlag.AlignTop)
        

        # add our left panel widgets
        left_pane.addWidget(title_label)
        left_pane.addWidget(Height_label)
        left_pane.addWidget(self.Height_Spinbox)
        left_pane.addWidget(Length_label)
        left_pane.addWidget(self.Length_Spinbox)
        left_pane.addWidget(Width_label)
        left_pane.addWidget(self.Width_Spinbox)
        left_pane.addWidget(self.calculate_button)

        # add our right pane widgets
        right_pane.addWidget(results_title)
        right_pane.addWidget(label)
        right_pane.addWidget(self.results_window)


        # add the two panes to the layout
        main_layout.addLayout(left_pane)
        main_layout.addLayout(right_pane)

        # set the main Layout
        gui = QWidget()
        gui.setLayout(main_layout)
        self.setCentralWidget(gui)
    
    def calculate_volume(self):
        """Calculate Volume"""
        #Get Length
        Length = self.Length_Spinbox.value()
        
        #Get Width
        Width = self.Width_Spinbox.value()

        #Get Height
        Height = self.Height_Spinbox.value()

        #Get Volume
        results = controller.get_volume(Length, Width, Height)

        #Display results
        self.results_window.setText(results)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    controller

    app.exec()
    