import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

def main():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setWindowTitle("Başlık")
    win.setGeometry(1500,500,1000,700)
    win.show()
    sys.exit(app.exec())
0
main()