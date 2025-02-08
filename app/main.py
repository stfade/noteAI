import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QFont, QIcon
from gui import FileUploadGUI
from utils import get_resource_path

def main():
    app = QApplication(sys.argv)
    app.setFont(QFont('Cascadia Mono SemiBold'))

    # Set window icon properly
    icon_path = get_resource_path("app/assets/app-icon.ico")
    app.setWindowIcon(QIcon(icon_path))

    gui = FileUploadGUI()
    gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
