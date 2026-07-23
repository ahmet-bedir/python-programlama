import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

def main():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.show()
    sys.exit(app.exec())

main()