# gui.py
from PyQt5.QtWidgets import (QMainWindow, QPushButton, QLabel, 
                           QVBoxLayout, QHBoxLayout, QWidget, QFileDialog,
                           QFrame, QApplication) # pip install pyqt5
from PyQt5.QtCore import Qt # pip install pyqt5
from styles import MAIN_STYLE, TITLE_STYLE, STATUS_STYLE

from logic import process_logic

import time

class FileUploadGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pdf_path = None
        self.image_path = None

        self.initUI()

    def getPdfPath(self):
        return self.pdf_path
    
    def getImagePath(self):
        return self.image_path

    def initUI(self):
        self.setWindowTitle('noteAI')
        self.setGeometry(500, 160, 800, 600)
        self.setStyleSheet(MAIN_STYLE)
        
        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(30, 30, 30, 30)
        
        # Create title label
        title_label = QLabel('noteAI 🧠')
        title_label.setStyleSheet(TITLE_STYLE)
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)
        
        self._setup_upload_frame(main_layout)
        self._setup_status_section(main_layout)
        self._connect_buttons()
        
    def _setup_upload_frame(self, main_layout):
        upload_frame = QFrame()
        upload_layout = QVBoxLayout(upload_frame)
        
        # PDF section
        pdf_section = QWidget()
        pdf_layout = QHBoxLayout(pdf_section)
        self.pdf_label = QLabel('No PDF file selected')
        self.pdf_button = QPushButton('📄 Upload PDF', self)
        pdf_layout.addWidget(self.pdf_label, stretch=1)
        pdf_layout.addWidget(self.pdf_button)
        
        # Image section
        image_section = QWidget()
        image_layout = QHBoxLayout(image_section)
        self.image_label = QLabel('No image file selected')
        self.image_button = QPushButton('🖼 Upload Image', self)
        image_layout.addWidget(self.image_label, stretch=1)
        image_layout.addWidget(self.image_button)
        
        # Process button
        self.process_button = QPushButton('▶ Start Process', self)
        self.process_button.setObjectName("processButton")
        self.process_button.setEnabled(False)
        
        # Add sections to upload frame
        upload_layout.addWidget(pdf_section)
        upload_layout.addWidget(image_section)
        upload_layout.addWidget(self.process_button, alignment=Qt.AlignCenter)
        
        main_layout.addWidget(upload_frame)

    def _setup_status_section(self, main_layout):
        self.status_label = QLabel('Please upload PDF and image file to start processing...')
        self.status_label.setStyleSheet(STATUS_STYLE)
        self.status_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.status_label)

    def _connect_buttons(self):
        self.pdf_button.clicked.connect(self.upload_pdf)
        self.image_button.clicked.connect(self.upload_image)
        self.process_button.clicked.connect(self.process_start)

    def upload_pdf(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Select PDF File", "", "PDF Files (*.pdf)"
        )
        if file_name:
            self.pdf_path = file_name
            self.pdf_label.setText(f'Selected: {file_name.split("/")[-1]}')
            self.pdf_label.setStyleSheet("color: #27ae60; font-weight: bold;")
            self.check_process_button()
            self.status_label.setText('PDF file uploaded successfully')
            
    def upload_image(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Select Image File", "", "Image Files (*.png *.jpg *.jpeg)"
        )
        if file_name:
            self.image_path = file_name
            self.image_label.setText(f'Selected: {file_name.split("/")[-1]}')
            self.image_label.setStyleSheet("color: #27ae60; font-weight: bold;")
            self.check_process_button()
            self.status_label.setText('Image file uploaded successfully')
            
    def check_process_button(self):
        if self.pdf_path and self.image_path:
            self.process_button.setEnabled(True)
            self.status_label.setText('Ready to process files')

    def process_start(self):
        # Disable process button during processing
        self.process_button.setEnabled(False)
        
        # Update status label
        self.status_label.setStyleSheet("""
            background-color: #789DBC;
            color: white;
            padding: 10px;
            border-radius: 5px;
            font-size: 16px;
        """)
        self.status_label.setText('Processing files, please wait until done....')

        # Force the UI to update
        QApplication.processEvents()
        
        try:
            # Call processing logic
            process_logic(self.pdf_path, self.image_path)
            # time.sleep(3)  # Simulate processing time
        except Exception as e:
            # Handle any processing errors
            self.status_label.setStyleSheet("""
                background-color: #e74c3c;
                color: white;
                padding: 10px;
                border-radius: 5px;
                font-size: 12px;
            """)
            self.status_label.setText(f'Processing failed: {str(e)}')
        finally:
            # Re-enable process button
            self.process_button.setEnabled(True)
            self.process_done()

    def process_done(self):
        # Update status label
        self.status_label.setStyleSheet("""
            background-color: #A0C878;
            color: white;
            padding: 10px;
            border-radius: 5px;
            font-size: 12px;
        """)
        self.status_label.setText('Files processed successfully!')