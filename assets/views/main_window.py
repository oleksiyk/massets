# assets/views/main_window.py

from PyQt6.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt6.QtGui import QAction
from sqlalchemy.orm import Session
from assets.models import Asset

class MainWindow(QMainWindow):
    def __init__(self, Session, engine):
        super().__init__()

        self.setWindowTitle("Asset Manager")
        self.setGeometry(100, 100, 800, 600)

        # Database session
        self.session: Session = Session()

        # Main layout
        self.main_widget = QWidget()
        self.main_layout = QVBoxLayout()
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)

        # Initialize UI components
        self.init_menu()
        self.init_table_widget()

        # Load data into the table
        self.load_assets()

    def init_menu(self):
        """
        Sets up the menu bar.
        """
        menubar = self.menuBar()

        # File Menu
        file_menu = menubar.addMenu("File")
        export_action = QAction("Export to Excel", self)
        export_action.triggered.connect(self.export_to_excel)
        file_menu.addAction(export_action)

        # Sync Menu
        sync_menu = menubar.addMenu("Sync")
        sync_action = QAction("Sync with Google Sheets", self)
        sync_action.triggered.connect(self.sync_with_google_sheets)
        sync_menu.addAction(sync_action)

    def init_table_widget(self):
        """
        Initializes the QTableWidget to display assets.
        """
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(4)
        self.table_widget.setHorizontalHeaderLabels(["ID", "Name", "Category", "Status"])
        self.main_layout.addWidget(self.table_widget)

    def load_assets(self):
        """
        Loads asset data from the database into the QTableWidget.
        """
        assets = self.session.query(Asset).all()
        self.table_widget.setRowCount(len(assets))
        for row_index, asset in enumerate(assets):
            self.table_widget.setItem(row_index, 0, QTableWidgetItem(str(asset.id)))
            self.table_widget.setItem(row_index, 1, QTableWidgetItem(asset.name))
            self.table_widget.setItem(row_index, 2, QTableWidgetItem(asset.category))
            self.table_widget.setItem(row_index, 3, QTableWidgetItem(asset.status))

    def export_to_excel(self):
        """
        Exports asset data to an Excel file.
        """
        print("Export to Excel functionality")

    def sync_with_google_sheets(self):
        """
        Syncs data with Google Sheets.
        """
        print("Sync with Google Sheets functionality")
