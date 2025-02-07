# styles.py
MAIN_STYLE = """
    QMainWindow {
        background-color: #f0f2f5;
    }
    QLabel {
        color: #2c3e50;
        font-size: 16px;
        padding: 5px;
    }
    QPushButton {
        background-color: #3498db;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        font-size: 18px;
        min-width: 150px;
    }
    QPushButton:hover {
        background-color: #2980b9;
    }
    QPushButton:disabled {
        background-color: #E5E1DA;
    }
    QPushButton#processButton {
        background-color: #6A80B9;
        font-weight: bold;
    }
    QPushButton#processButton:hover {
        background-color: #155E95;
    }
    QPushButton#processButton:disabled {
        background-color: #f0f2f5;
        color: #5C7285;
    }
    QFrame {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
    }
"""

TITLE_STYLE = """
    font-size: 36px;
    color: #2c3e50;
    font-weight: bold;
    padding: 10px;
"""

STATUS_STYLE = """
    background-color: white;
    padding: 10px;
    border-radius: 5px;
    color: #7f8c8d;
"""