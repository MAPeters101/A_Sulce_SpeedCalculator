import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, \
    QLineEdit, QPushButton, QComboBox

class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SpeedCalculator")
        grid = QGridLayout()

        # Create widgets
        distance_label = QLabel("Distance:")
        self.distance_line_edit = QLineEdit()

        time_label = QLabel("Time (hours):")
        self.time_line_edit = QLineEdit()

        calculate_button = QPushButton("Calculate Speed")
        calculate_button.clicked.connect(self.calculate_speed)
        self.output_label = QLabel("")


        # Add widgets to grid
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate_speed(self):
        speed = float(self.distance_line_edit.text()) / float(self.time_line_edit.text())
        self.output_label.setText(f"The speed was {speed}.")


app = QApplication(sys.argv)
speed_calculator = SpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())
