import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QFont, QIcon
from gui import FileUploadGUI
import os

def main():
    app = QApplication(sys.argv)
    app.setFont(QFont('Cascadia Mono SemiBold'))

    # Construct an absolute path to the icon (adjust if needed)
    current_dir = os.path.dirname(os.path.realpath(__file__))
    icon_path = os.path.join(current_dir, 'assets', 'app-icon.png')

    # Set the app icon
    app.setWindowIcon(QIcon(icon_path))

    gui = FileUploadGUI()
    gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
